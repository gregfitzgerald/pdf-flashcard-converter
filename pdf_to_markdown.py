#!/usr/bin/env python3
"""
PDF to Markdown Converter
Converts PDF articles to markdown format for manual flashcard creation
"""

import os
import sys
import argparse
import platform
from pathlib import Path
import PyPDF2
import pdfplumber
from pathvalidate import sanitize_filename

class PDFToMarkdownConverter:
    def __init__(self):
        pass
    
    def extract_text_from_pdf(self, pdf_path):
        """Extract text from PDF using multiple methods for robustness"""
        text = ""
        
        # Try pdfplumber first (better for complex layouts and tables)
        try:
            with pdfplumber.open(pdf_path) as pdf:
                for page_num, page in enumerate(pdf.pages, 1):
                    page_text = page.extract_text()
                    if page_text:
                        text += f"\n\n--- Page {page_num} ---\n"
                        text += page_text + "\n"
                    
                    # Also extract tables if present
                    tables = page.extract_tables()
                    if tables:
                        text += f"\n### Tables on Page {page_num}:\n"
                        for table_num, table in enumerate(tables, 1):
                            text += f"\n**Table {table_num}:**\n"
                            for row in table:
                                if row:  # Skip empty rows
                                    text += "| " + " | ".join(str(cell) if cell else "" for cell in row) + " |\n"
                            text += "\n"
                        
        except Exception as e:
            print(f"pdfplumber failed: {e}")
            
        # Fallback to PyPDF2 if pdfplumber fails or returns little text
        if len(text.strip()) < 500:
            try:
                with open(pdf_path, 'rb') as file:
                    pdf_reader = PyPDF2.PdfReader(file)
                    text = ""
                    for page_num in range(len(pdf_reader.pages)):
                        page = pdf_reader.pages[page_num]
                        page_text = page.extract_text()
                        if page_text:
                            text += f"\n\n--- Page {page_num + 1} ---\n"
                            text += page_text + "\n"
            except Exception as e:
                print(f"PyPDF2 also failed: {e}")
                return None
        
        return text.strip() if text.strip() else None
    
    def convert_to_markdown(self, text, pdf_path):
        """Convert extracted text to markdown format"""
        pdf_name = Path(pdf_path).stem
        
        # Create markdown header
        markdown = f"# {pdf_name}\n\n"
        markdown += f"**Source:** {Path(pdf_path).name}\n"
        markdown += f"**Converted:** {__import__('datetime').datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n"
        markdown += "---\n\n"
        
        # Clean up the text and format as markdown
        lines = text.split('\n')
        in_references = False
        
        for line in lines:
            line = line.strip()
            
            # Skip empty lines
            if not line:
                markdown += "\n"
                continue
            
            # Handle page separators
            if line.startswith("--- Page"):
                markdown += f"\n{line}\n\n"
                continue
            
            # Handle table headers
            if line.startswith("### Tables"):
                markdown += f"{line}\n"
                continue
                
            if line.startswith("**Table"):
                markdown += f"\n{line}\n"
                continue
            
            # Handle table rows
            if line.startswith("| ") and line.endswith(" |"):
                markdown += f"{line}\n"
                continue
            
            # Detect sections (common academic paper sections)
            if line.upper() in ['ABSTRACT', 'INTRODUCTION', 'METHODS', 'RESULTS', 
                               'DISCUSSION', 'CONCLUSION', 'REFERENCES', 'ACKNOWLEDGMENTS']:
                markdown += f"\n## {line.title()}\n\n"
                if line.upper() == 'REFERENCES':
                    in_references = True
                continue
            
            # Handle references section formatting
            if in_references:
                # Basic reference formatting
                if any(char.isdigit() for char in line[:10]):  # Likely a numbered reference
                    markdown += f"\n{line}\n"
                else:
                    markdown += f"{line} "
                continue
            
            # Handle potential subsections (lines that are short and likely headers)
            if len(line) < 100 and not line.endswith('.') and not line.endswith(','):
                # Check if it might be a subsection header
                words = line.split()
                if len(words) <= 8 and any(word[0].isupper() for word in words):
                    markdown += f"\n### {line}\n\n"
                    continue
            
            # Regular paragraph text
            markdown += f"{line} "
            
            # Add paragraph breaks for sentences that end with periods
            if line.endswith('.'):
                markdown += "\n\n"
        
        return markdown
    
    def process_pdf(self, pdf_path, output_name=None):
        """Main method to process a PDF and convert to markdown"""
        # Validate PDF path
        if not os.path.exists(pdf_path):
            print(f"Error: PDF file not found: {pdf_path}")
            return False
        
        print(f"Processing PDF: {pdf_path}")
        
        # Extract text from PDF
        text = self.extract_text_from_pdf(pdf_path)
        if not text:
            print("Error: Could not extract text from PDF")
            return False
        
        print(f"Extracted {len(text)} characters from PDF")
        
        # Convert to markdown
        markdown_content = self.convert_to_markdown(text, pdf_path)
        
        # Determine output filename
        if not output_name:
            pdf_name = Path(pdf_path).stem
            output_name = f"{sanitize_filename(pdf_name)}.md"
        
        output_path = Path(__file__).parent / output_name
        
        # Save markdown file
        try:
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(markdown_content)
            
            print(f"Markdown saved to: {output_path}")
            
            # Provide Windows path for easy access
            if platform.system() == "Linux":
                win_path = str(output_path).replace('/mnt/c/', 'C:\\').replace('/', '\\')
                print(f"Windows path: {win_path}")
            
            return True
            
        except Exception as e:
            print(f"Error saving markdown: {e}")
            return False

def main():
    parser = argparse.ArgumentParser(description='Convert PDF articles to markdown format')
    parser.add_argument('pdf_path', help='Path to the PDF file or directory containing PDFs')
    parser.add_argument('-o', '--output', help='Output filename (optional)')
    
    args = parser.parse_args()
    
    try:
        converter = PDFToMarkdownConverter()
        
        # Check if input is a file or directory
        if os.path.isfile(args.pdf_path):
            # Process single PDF
            success = converter.process_pdf(args.pdf_path, args.output)
            sys.exit(0 if success else 1)
            
        elif os.path.isdir(args.pdf_path):
            # Process all PDFs in directory
            pdf_files = [f for f in os.listdir(args.pdf_path) if f.lower().endswith('.pdf')]
            
            if not pdf_files:
                print(f"No PDF files found in {args.pdf_path}")
                sys.exit(1)
            
            print(f"Found {len(pdf_files)} PDF files")
            
            success_count = 0
            for pdf_file in pdf_files:
                pdf_path = os.path.join(args.pdf_path, pdf_file)
                print(f"\n--- Processing {pdf_file} ---")
                
                if converter.process_pdf(pdf_path):
                    success_count += 1
                else:
                    print(f"Failed to process {pdf_file}")
            
            print(f"\nCompleted: {success_count}/{len(pdf_files)} PDFs processed successfully")
            sys.exit(0 if success_count > 0 else 1)
            
        else:
            print(f"Error: {args.pdf_path} is not a valid file or directory")
            sys.exit(1)
            
    except Exception as e:
        print(f"Unexpected error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()