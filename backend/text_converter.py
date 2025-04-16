import os
from PyPDF2 import PdfReader

PDF_DIR = "data/resumes"
TXT_DIR = "data/text_resumes"

os.makedirs(TXT_DIR, exist_ok=True)

for pdf_file in os.listdir(PDF_DIR):
    if pdf_file.endswith(".pdf"):
        reader = PdfReader(os.path.join(PDF_DIR, pdf_file))
        #text = "\n".join([page.extract_text() for page in reader.pages])
        text = "\n".join([page.extract_text() or "" for page in reader.pages])
        #with open(os.path.join(TXT_DIR, pdf_file.replace(".pdf", ".txt")), "w") as f:
        with open(os.path.join(TXT_DIR, pdf_file.replace(".pdf", ".txt")), "w", encoding="utf-8") as f:
            f.write(text)

# Resume Dataset: https://www.kaggle.com/datasets/snehaanbhawal/resume-dataset