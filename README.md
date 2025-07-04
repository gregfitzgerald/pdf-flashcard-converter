# PDF to Markdown Converter for Flashcard Generation

## Project Overview

This repository converts PDF research articles into markdown format for manual flashcard creation. **NO AI APIs required** -- this is a simple Python-based PDF text extraction tool.

## User Requirements Recap

Based on your specifications:
- **Input:** PDF articles or paths to PDF articles
- **Output:** Markdown files that can be manually reviewed and converted to flashcards
- **Environment:** Windows 11 with WSL
- **No AI APIs:** Pure Python library approach using pdfplumber and PyPDF2
- **No emoji:** Clean, professional output
- **Cross-platform paths:** Forward slashes for Windows paths (C:/Users/...)

## Features

- Extract text from PDF articles using robust Python libraries (pdfplumber + PyPDF2 fallback)
- Convert extracted text to clean markdown format with proper structure
- Preserve tables and page structure where possible
- Process single PDFs or batch process entire directories
- Cross-platform support (Windows/WSL)
- No internet connection or API keys required

## Setup

1. Install Python dependencies:
```bash
pip install -r requirements.txt
```

**No environment variables or API keys needed!**

## Usage

### Single PDF Processing
```bash
python pdf_to_markdown.py path/to/article.pdf
```

### Custom Output Name
```bash
python pdf_to_markdown.py article.pdf -o custom_name.md
```

### Batch Processing (Directory)
```bash
python pdf_to_markdown.py path/to/pdf/directory/
```

### Windows Path Examples (as per your requirements)
```bash
# Single file
python pdf_to_markdown.py "C:/Users/gregs/Documents/research_paper.pdf"

# Directory
python pdf_to_markdown.py "C:/Users/gregs/Documents/research_papers/"
```

## Output Format

The script generates clean markdown files with:
- Document title and metadata header
- Structured sections (Abstract, Introduction, Methods, Results, etc.)
- Preserved page numbers for reference
- Table extraction when present
- Clean paragraph formatting

## Workflow for Flashcard Creation

1. **Convert PDF to Markdown:**
   ```bash
   python pdf_to_markdown.py "C:/path/to/research_paper.pdf"
   ```

2. **Review the Generated Markdown:**
   - Open the `.md` file in your preferred editor
   - Review the extracted content for accuracy
   - Note any formatting issues or missing sections

3. **Create Flashcards Manually:**
   - Use your existing `templates_prompts/master_flashcard_prompt.md` as a guide
   - Extract key information following your established format:
     - Front: Specific, testable questions with quantitative details
     - Back: Complete, precise answers with numbers and percentages
     - Context: Detailed background serving as paper substitute

4. **Import to Anki:**
   - Save flashcards in CSV format: `Front,Back,Context`
   - Import into Anki using File → Import

## File Structure

```
flaschard generation/
├── pdf_to_markdown.py             # Main conversion script
├── requirements.txt                # Python dependencies (NO API libraries)
├── templates_prompts/
│   └── master_flashcard_prompt.md # Your flashcard generation template
├── *.csv                          # Your existing flashcard files
└── *.md                           # Generated markdown files
```

## Python Libraries Used

- **pdfplumber**: Primary PDF text extraction (handles complex layouts and tables)
- **PyPDF2**: Fallback PDF extraction method
- **pathvalidate**: Clean filename generation
- **argparse**: Command-line interface

**No AI API dependencies** -- completely offline operation.

## Troubleshooting

- **Empty Output**: Check if the PDF contains extractable text (not just scanned images)
- **Formatting Issues**: pdfplumber handles most layouts; PyPDF2 provides fallback
- **Table Extraction**: Tables are extracted when detectable by pdfplumber
- **Path Issues**: Use forward slashes for Windows paths: `C:/Users/...`

## Important Notes

- **Manual Review Required**: Always review the markdown output before creating flashcards
- **Quality Control**: The extraction preserves source text but may need manual cleanup
- **No Automatic Flashcard Generation**: This tool only converts PDF to markdown; flashcard creation remains manual as per your workflow
- **Cross-Platform**: Scripts work in Windows WSL environment as specified

## Your Existing Flashcard Template

Your `master_flashcard_prompt.md` template remains the gold standard for flashcard quality. Use the generated markdown as source material to create flashcards following your established guidelines:

- 20 high-quality flashcards per paper
- 4-5 cards each for: findings, methods, terminology, statistics, limitations
- Specific questions with quantitative details
- Complete answers with effect sizes and significance levels
- Detailed context fields serving as paper substitutes

This workflow maintains your quality standards while streamlining the initial text extraction step.