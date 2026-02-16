# PDF Classifier — Smarter · Leaner · Swifter

A simple Flask web app that displays PDFs from a directory and lets you classify each one with three checkboxes: **Smarter**, **Leaner**, **Swifter**. Classifications are saved to a CSV file.

## Setup

```bash
pip install flask
```

## Usage

1. Put your PDF files in the `pdfs/` directory (or set `PDF_DIR` env var to point elsewhere)
2. Run the app:

```bash
python app.py
```

3. Open http://localhost:5000

## Features

- PDF viewer with sidebar navigation
- Three checkboxes per PDF (Smarter, Leaner, Swifter)
- Auto-saves to `classifications.csv` on every check
- Progress tracker showing how many PDFs have been classified
- Keyboard shortcuts: `←/→` to navigate, `1/2/3` to toggle checkboxes
- Colored dots in the sidebar show which tags are applied

## CSV Output

The `classifications.csv` file has four columns:

| pdf_name | smarter | leaner | swifter |
|----------|---------|--------|---------|
| paper.pdf | True | False | True |
