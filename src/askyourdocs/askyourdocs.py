import pypdf

reader = pypdf.PdfReader("UGWUMBA-NWOYE_MICHAEL_FINAL_YEAR_PROJECT_v2.pdf")

print(len(reader.pages))

page_text = reader.pages[0].extract_text()

print(page_text)
