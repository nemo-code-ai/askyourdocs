import pypdf

reader = pypdf.PdfReader("users\UGWUMBA-NWOYE_MICHAEL_FINAL_YEAR_PROJECT_v2.pdf")

print(len(reader.pages))

page_text = reader.pages[0].extract_text()

print(page_text)

full_text = ""

for page in reader.pages:
    full_text += page.extract_text() + "\n\n"

print(f"Total characters: {len(full_text)}")