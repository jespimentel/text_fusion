import os
import fitz  # PyMuPDF
from docx import Document

def extract_text_from_pdf(pdf_path):
    text = ""
    try:
        document = fitz.open(pdf_path)
        for page_num in range(len(document)):
            page = document.load_page(page_num)
            text += page.get_text()
        document.close()
    except Exception as e:
        text = f"Error reading PDF file {pdf_path}: {e}\n"
    return text

def extract_text_from_docx(docx_path):
    text = ""
    try:
        document = Document(docx_path)
        for paragraph in document.paragraphs:
            text += paragraph.text + "\n"
    except Exception as e:
        text = f"Error reading DOCX file {docx_path}: {e}\n"
    return text

def extract_text_from_txt(txt_path):
    text = ""
    try:
        with open(txt_path, 'r', encoding='utf-8') as file:
            text = file.read()
    except Exception as e:
        text = f"Error reading TXT file {txt_path}: {e}\n"
    return text

def clean_text(text):
    # Remove multiple newlines and excess spaces
    lines = text.split('\n')
    cleaned_lines = [line.strip() for line in lines if line.strip() != ""]
    cleaned_text = ' '.join(cleaned_lines)
    return cleaned_text

def write_to_output(file_path, text, output_file):
    with open(output_file, 'a', encoding='utf-8') as file:
        file.write(f"Arquivo: {file_path}\n")
        file.write(clean_text(text) + "\n")
        file.write("FIM DO ARQUIVO\n\n")

def process_directory(directory, output_file):
    for root, _, files in os.walk(directory):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            if file_path.endswith('.pdf'):
                text = extract_text_from_pdf(file_path)
                write_to_output(file_path, text, output_file)
            elif file_path.endswith('.docx'):
                text = extract_text_from_docx(file_path)
                write_to_output(file_path, text, output_file)
            elif file_path.endswith('.txt'):
                text = extract_text_from_txt(file_path)
                write_to_output(file_path, text, output_file)

if __name__ == "__main__":
    input_directory = 'documentos' # modifique, se necessário
    output_file = 'arquivos_gerados/output.txt'
    process_directory(input_directory, output_file)