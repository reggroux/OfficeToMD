# docx2md

A small, local-first DOCX to Markdown converter.

## Setup

1. Create and activate the virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

2. Install the package:

```bash
python -m pip install -e .
```

## Usage

Convert a file:

```bash
docx2md "Price Sheet Chat.docx"
```

Choose an output path:

```bash
docx2md "Price Sheet Chat.docx" -o output.md
```

Write to stdout:

```bash
docx2md "Price Sheet Chat.docx" --stdout
```
