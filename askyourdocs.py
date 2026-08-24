import pypdf

def extract_pdf_text(file_path):
    reader = pypdf.PdfReader(file_path)

    full_text = ""
    for page in reader.pages:
        full_text += (page.extract_text() or "") + "\n\n"

    for page in reader.pages:
    text = page.extract_text()

    text = text.strip()

    chunks = text.split("\n\n")

    return full_text



