from flask import Flask, render_template, request
import os
import PyPDF2
import pdfplumber
import camelot
from pdfminer.high_level import extract_text
from tika import parser
import pytesseract
from pdf2image import convert_from_path

app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return "No file part"

    file = request.files['file']
    if file.filename == '':
        return "No selected file"

    file_path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(file_path)

    text = extract_pdf_text(file_path)
    return render_template('result.html', text=text)


def extract_pdf_text(pdf_path):
    extracted_text = ""

    # PyPDF2
    with open(pdf_path, "rb") as file:
        reader = PyPDF2.PdfReader(file)
        for page in reader.pages:
            extracted_text += page.extract_text() + "\n"

    # PDFMiner
    extracted_text += "\nPDFMiner Extracted Text:\n" + extract_text(pdf_path)

    # pdfplumber
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            extracted_text += "\nPDFPlumber:\n" + page.extract_text()

    # Apache Tika
    parsed_pdf = parser.from_file(pdf_path)
    if parsed_pdf['content']:
        extracted_text += "\nTika Extracted Text:\n" + parsed_pdf['content']
    else:
        extracted_text += "\nTika Extracted Text: No text extracted\n"

    # Camelot (for extracting tables)
    tables = camelot.read_pdf(pdf_path)
    if tables.n > 0:
        extracted_text += "\nExtracted Tables:\n" + tables[0].df.to_string()

    # OCR (Tesseract) if scanned PDF
    images = convert_from_path(pdf_path)
    for img in images:
        extracted_text += "\nOCR Extracted Text:\n" + pytesseract.image_to_string(img)

    return extracted_text


if __name__ == '__main__':
    app.run(debug=True)
