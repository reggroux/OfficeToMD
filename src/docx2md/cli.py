from __future__ import annotations

import argparse
from pathlib import Path
from typing import Optional

import mammoth
from markdownify import markdownify as md


def convert_docx_to_markdown(input_path: Path) -> str:
    with input_path.open("rb") as docx_file:
        result = mammoth.convert_to_html(docx_file)

    html = result.value
    markdown = md(html, heading_style="ATX")
    return markdown.rstrip() + "\n"


def parse_args(argv: Optional[list[str]] = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Convert a .docx file to Markdown."
    )
    parser.add_argument("input", type=Path, help="Path to input .docx file")
    parser.add_argument(
        "-o",
        "--output",
        type=Path,
        help="Path to output .md file (defaults to input basename)",
    )
    parser.add_argument(
        "--stdout",
        action="store_true",
        help="Write Markdown to stdout instead of a file",
    )
    return parser.parse_args(argv)


def main(argv: Optional[list[str]] = None) -> int:
    args = parse_args(argv)
    input_path: Path = args.input

    if not input_path.exists():
        raise SystemExit(f"Input file not found: {input_path}")
    if input_path.suffix.lower() != ".docx":
        raise SystemExit("Input file must be a .docx file")

    markdown = convert_docx_to_markdown(input_path)

    if args.stdout:
        print(markdown, end="")
        return 0

    output_path: Path = args.output or input_path.with_suffix(".md")
    output_path.write_text(markdown, encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
