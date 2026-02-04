# OfficeToMD

A small, local-first Office to Markdown converter. It is intended to support
all Office file types in the future, but currently only works with Word
`*.docx` files.

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
officetomd "Price Sheet Chat.docx"
```

Choose an output path:

```bash
officetomd "Price Sheet Chat.docx" -o output.md
```

Write to stdout:

```bash
officetomd "Price Sheet Chat.docx" --stdout
```
