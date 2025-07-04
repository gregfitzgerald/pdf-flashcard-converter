# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Purpose

This is a PDF-to-markdown converter designed for academic flashcard creation workflow. The repository converts PDF research articles into clean markdown format for manual review and flashcard generation. **No AI APIs are used** -- this is purely Python-based text extraction.

## Environment Requirements

- **Target Environment**: Windows 11 with WSL
- **Path Format**: Use forward slashes for Windows paths: `C:/Users/...`
- **Python**: Uses Python 3 with offline libraries only
- **No API Keys**: No environment variables or API configurations needed

## Core Architecture

The system has a simple two-stage workflow:
1. **PDF Extraction**: `pdf_to_markdown.py` extracts text using pdfplumber (primary) with PyPDF2 fallback
2. **Manual Flashcard Creation**: Users manually create flashcards using the generated markdown and existing quality template

### Key Components

- `PDFToMarkdownConverter` class handles dual-method text extraction (pdfplumber + PyPDF2)
- Table extraction preserves structured data from PDFs
- Section detection identifies academic paper structure (Abstract, Methods, Results, etc.)
- Cross-platform path handling for Windows/WSL environment

## Common Commands

### Setup and Dependencies
```bash
pip install -r requirements.txt
```

### PDF Processing
```bash
# Single PDF
python pdf_to_markdown.py "path/to/article.pdf"

# Custom output name
python pdf_to_markdown.py article.pdf -o custom_name.md

# Batch processing (directory)
python pdf_to_markdown.py "path/to/pdf/directory/"

# Windows path format (as required)
python pdf_to_markdown.py "C:/Users/gregs/Documents/research_paper.pdf"
```

### Testing Script Functionality
```bash
python pdf_to_markdown.py --help
```

## Flashcard Quality Standards

The repository maintains existing high-quality flashcard standards defined in `templates_prompts/master_flashcard_prompt.md`:
- 20 flashcards per paper (4-5 each: findings, methods, terminology, statistics, limitations)
- CSV format: `Front,Back,Context`
- Specific questions with quantitative details
- Complete answers with effect sizes and significance levels
- Detailed context serving as paper substitute

## Output Files

- **Generated Markdown**: `*.md` files for manual review
- **Existing Flashcards**: `*_flashcards.csv` files (examples of quality standards)
- **Template**: `templates_prompts/master_flashcard_prompt.md` (quality reference)

## Development Notes

- Text extraction uses dual fallback system for robustness
- Academic paper section detection handles common structures
- Table extraction preserves data when detectable
- Path sanitization ensures clean output filenames
- No internet connectivity required (fully offline operation)