#!/usr/bin/env python
"""First-pass audit for Chinese TCM theory discussion manuscripts.

Usage:
  python audit_manuscript.py manuscript.docx
  python audit_manuscript.py manuscript.txt
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path


RISK_PHRASES = [
    "本文认为",
    "由此可见",
    "该理论",
    "我们可以理解为",
    "二者虽分属不同体系",
    "既往《中医学报》相关研究",
    "例如",
    "譬如",
    "不宜",
]

MODULE_HEADINGS = [
    "理论基础",
    "病机分析",
    "现代机制",
    "治疗思路",
    "治疗策略",
    "方药配伍",
    "机制探讨",
    "临床启示",
]

DRAFT_MARKERS = ["【", "】", "TODO", "待补", "待查", "这里", "注意："]


def read_docx(path: Path) -> tuple[list[str], list[str]]:
    try:
        from docx import Document
    except Exception as exc:  # pragma: no cover - environment dependent
        raise SystemExit(f"python-docx is required for DOCX input: {exc}") from exc

    doc = Document(str(path))
    paragraphs: list[str] = []
    headings: list[str] = []
    for p in doc.paragraphs:
        text = p.text.strip()
        if not text:
            continue
        paragraphs.append(text)
        style_name = p.style.name if p.style is not None else ""
        if style_name.startswith("Heading"):
            headings.append(text)
    return paragraphs, headings


def read_text(path: Path) -> tuple[list[str], list[str]]:
    text = path.read_text(encoding="utf-8-sig")
    paragraphs = [line.strip() for line in text.splitlines() if line.strip()]
    heading_pattern = re.compile(r"^(\d+[\.\s、]|[一二三四五六七八九十]+[、．.])")
    headings = [p for p in paragraphs if heading_pattern.match(p)]
    return paragraphs, headings


def count_citations(text: str) -> dict[str, object]:
    citation_numbers: set[int] = set()
    for match in re.finditer(r"\[([0-9,\-]+)\]", text):
        for part in match.group(1).split(","):
            if re.fullmatch(r"\d+", part):
                citation_numbers.add(int(part))
            elif re.fullmatch(r"\d+-\d+", part):
                start, end = map(int, part.split("-"))
                citation_numbers.update(range(start, end + 1))
    return {
        "count": len(citation_numbers),
        "numbers": sorted(citation_numbers),
    }


def main() -> int:
    if len(sys.argv) != 2:
        print(__doc__.strip(), file=sys.stderr)
        return 2

    path = Path(sys.argv[1])
    if not path.exists():
        print(f"Input not found: {path}", file=sys.stderr)
        return 2

    if path.suffix.lower() == ".docx":
        paragraphs, headings = read_docx(path)
    else:
        paragraphs, headings = read_text(path)

    full_text = "\n".join(paragraphs)
    heading_text = "\n".join(headings)
    result = {
        "file": str(path),
        "paragraph_count": len(paragraphs),
        "heading_count": len(headings),
        "char_count": len(full_text),
        "headings": headings,
        "risk_phrase_hits": {
            phrase: full_text.count(phrase)
            for phrase in RISK_PHRASES
            if full_text.count(phrase)
        },
        "module_heading_hits": {
            phrase: heading_text.count(phrase)
            for phrase in MODULE_HEADINGS
            if heading_text.count(phrase)
        },
        "draft_marker_hits": {
            marker: full_text.count(marker)
            for marker in DRAFT_MARKERS
            if full_text.count(marker)
        },
        "citation_usage": count_citations(full_text),
        "contains_modern_mechanism_terms": any(
            term in full_text
            for term in ["内感受", "预测编码", "炎症", "菌群", "线粒体", "网络药理", "节律"]
        ),
        "contains_formula_terms": any(
            term in full_text
            for term in ["汤", "散", "丸", "方", "方药", "治宜", "治当"]
        ),
    }

    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
