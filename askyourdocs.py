import pypdf


def extract_pdf_text(file_path):
    reader = pypdf.PdfReader(file_path)

    full_text = ""
    for page in reader.pages:
        full_text += (page.extract_text() or "") + "\n\n"

    return full_text


extract_pdf_text(
    r"C:\Users\Michael Ugwumba\OneDrive\Desktop\RESUME PROJECTS\askyourdocs\UGWUMBA-NWOYE MICHAEL FINAL YEAR PROJECT v2.pdf"
)
