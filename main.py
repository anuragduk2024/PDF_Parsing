from flask import Flask, render_template, request, send_file, url_for
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
RESULTS_FOLDER = "parsed_results"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(RESULTS_FOLDER, exist_ok=True)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return "No file part"

    file = request.files['file']
    parser_option = request.form.get('parser_option')

    if file.filename == '':
        return "No selected file"

    # Save uploaded file
    file_path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(file_path)

    # Extract text based on selected parser
    extracted_text = extract_pdf_text(file_path, parser_option)

    # Save extracted text file
    result_filename = f"{parser_option}_{file.filename}.txt"
    result_file = os.path.join(RESULTS_FOLDER, result_filename)
    with open(result_file, "w", encoding="utf-8") as f:
        f.write(extracted_text)

    # Pass correct download link to template
    download_link = url_for('download_file', parser_option=parser_option, filename=file.filename)

    return render_template('result.html', text=extracted_text, download_link=download_link)


def extract_pdf_text(pdf_path, parser_option):
    extracted_text = ""

    if parser_option == "pypdf2":
        with open(pdf_path, "rb") as file:
            reader = PyPDF2.PdfReader(file)
            for page in reader.pages:
                extracted_text += page.extract_text() + "\n"

    elif parser_option == "pdfminer":
        extracted_text = extract_text(pdf_path)

    elif parser_option == "pdfplumber":
        with pdfplumber.open(pdf_path) as pdf:
            for page in pdf.pages:
                extracted_text += page.extract_text() + "\n"

    elif parser_option == "tika":
        parsed_pdf = parser.from_file(pdf_path)
        extracted_text = parsed_pdf.get('content', 'No text extracted')

    elif parser_option == "camelot":
        tables = camelot.read_pdf(pdf_path)
        if tables.n > 0:
            extracted_text = tables[0].df.to_string()

    elif parser_option == "ocr":
        images = convert_from_path(pdf_path)
        for img in images:
            extracted_text += pytesseract.image_to_string(img) + "\n"

    else:
        extracted_text = "Invalid parser option selected."

    return extracted_text


@app.route('/download/<parser_option>/<filename>')
def download_file(parser_option, filename):
    result_filename = f"{parser_option}_{filename}.txt"
    file_path = os.path.join(RESULTS_FOLDER, result_filename)

    if not os.path.exists(file_path):
        return f"Error: File {result_filename} not found at {file_path}", 404

    return send_file(file_path, as_attachment=True)


if __name__ == '__main__':
    app.run(debug=True)
