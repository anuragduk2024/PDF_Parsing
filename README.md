# PDF Parsing Flask Application

## Overview
This project is a Flask-based web application for extracting text from PDF files using various parsing techniques. Users can upload a PDF file, choose a parsing method, extract text, and download the extracted results.

## Major Changes in the `new-feature` Branch
The `new-feature` branch introduces several significant improvements over the `main` branch:

### 1. **Added Multiple Parsing Options**
- Implemented the ability to select different PDF parsers for text extraction.
- Supported parsers include:
  - `PyPDF2`
  - `pdfminer`
  - `pdfplumber`
  - `Tika`
  - `Camelot` (for table extraction)
  - `OCR` (using Tesseract for scanned PDFs)

### 2. **Enhanced Result Management**
- Each parser now saves its extracted text in a separate file within the `parsed_results/` directory.
- Filenames follow the format: `{parser_option}_{filename}.txt` to prevent overwriting results from different parsers.

### 3. **Implemented File Download Feature**
- Users can download the extracted text files directly from the results page.
- Flask's `send_file` function is used to serve the saved text files.

### 4. **Directory Structure Improvements**
- Ensured `uploads/` and `parsed_results/` directories are automatically created if they don’t exist.
- Fixed potential issues with incorrect file paths when saving and retrieving extracted text files.

### 5. **Bug Fixes**
- Resolved `FileNotFoundError` that occurred when attempting to download results due to incorrect file path references.
- Fixed incorrect nested `parsed_results/parsed_results/` directory issue.

## Installation and Usage
1. Clone the repository:
   ```bash
   git clone https://github.com/anuragduk2024/PDF_Parsing.git
   cd PDF_Parsing
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the Flask application:
   ```bash
   python main.py
   ```
4. Access the web interface at `http://127.0.0.1:5000/`.
5. Upload a PDF, choose a parser, extract text, and download results.

## Future Enhancements
- Add support for bulk PDF processing.
- Improve UI for better user experience.
- Implement more advanced NLP techniques for better text extraction.

## Contribution
If you wish to contribute:
1. Create a new branch:
   ```bash
   git checkout -b feature-branch
   ```
2. Make your changes and commit:
   ```bash
   git commit -m "Description of changes"
   ```
3. Push to GitHub and create a Pull Request.

---
### Author
**Anurag S S**

