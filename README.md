# PDF Parsing Web Application

## Overview
This project is a Flask-based web application that extracts text from PDF files using Apache Tika and Tesseract OCR. It allows users to upload PDFs and retrieve extracted text, supporting both standard and image-based PDFs.

## Features
- Extract text from standard PDFs using Apache Tika.
- Extract text from image-based PDFs using Tesseract OCR.
- Web-based interface for easy file uploads.
- Flask backend for processing and API handling.

## Technologies Used
- **Python** (Flask, PyTesseract, Requests)
- **Java** (Apache Tika)
- **Tesseract OCR**
- **HTML/CSS** (Frontend UI)

## Prerequisites
### 1. Install Java
Ensure that Java is installed and configured correctly:
```sh
java -version
```
If Java is not installed, download and install OpenJDK or Oracle JDK.

### 2. Install Apache Tika
Download and place the `tika-server-1.9.jar` in your project directory.
Start the Tika server:
```sh
java -jar tika-server-1.9.jar
```
Verify it's running at: `http://localhost:9998/`

### 3. Install Tesseract OCR
Download and install Tesseract OCR from [here](https://github.com/UB-Mannheim/tesseract/wiki).
After installation, add Tesseract to your system PATH:
```sh
setx PATH "%PATH%;C:\Program Files\Tesseract-OCR"
```
Verify the installation:
```sh
tesseract -v
```

### 4. Create a Virtual Environment
```sh
python -m venv PDF_P
```
Activate it:
```sh
# Windows
PDF_P\Scripts\activate

# macOS/Linux
source PDF_P/bin/activate
```

### 5. Install Dependencies
```sh
pip install -r requirements.txt
```

## Running the Application
1. Start the Tika server:
   ```sh
   java -jar tika-server-1.9.jar
   ```
2. Run the Flask application:
   ```sh
   python main.py
   ```
3. Open your browser and navigate to `http://127.0.0.1:5000/`.

## Troubleshooting
### 1. Java Not Recognized in PyCharm
- Ensure Java is installed and added to the system PATH.
- Restart PyCharm after configuring Java.
- Check the Java version inside the PyCharm terminal:
  ```sh
  java -version
  ```

### 2. `TypeError: can only concatenate str (not "NoneType") to str`
- This occurs when Apache Tika returns `None`. Ensure the Tika server is running properly.
- Try restarting the Tika server and re-uploading the PDF.

### 3. `TesseractNotFoundError: tesseract is not installed or it's not in your PATH`
- Ensure Tesseract OCR is installed and added to the PATH.
- Verify installation with:
  ```sh
  tesseract -v
  ```
- If the issue persists, manually set the Tesseract path in your Python script:
  ```python
  pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
  ```

## License
This project is open-source and available under the MIT License.

## Acknowledgements  

I would like to express my sincere gratitude to the following:  

- **OpenAI & Flask Community** – For providing extensive documentation and support that helped in developing the Flask-based web application.  
- **Apache Tika & Tesseract-OCR** – For enabling efficient text extraction from PDFs through robust open-source tools.  
- **Python & Open-Source Libraries** – For their rich ecosystem of tools that made implementation seamless.  
- **PyCharm & JetBrains** – For offering an efficient development environment.  
- **The Open-Source Community** – For continuous contributions and improvements in the field of text extraction and document processing.  
- **Friends & Mentors** – For guidance, testing, and valuable feedback throughout the project.  

I appreciate all the resources and contributions that made this project possible. 🚀  

## Author
ANURAG S S

