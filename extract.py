
# extract.py — pull text out of a PDF
from pypdf import PdfReader

def extract_text(pdf_path):
    reader = PdfReader(pdf_path)
    full_text = ""
    for i, page in enumerate(reader.pages):
        text = page.extract_text()
        if text:  # some pages can be empty (images only)
            full_text += f"\n--- Page {i+1} ---\n{text}"
    return full_text

if __name__ == "__main__":
    text = extract_text("sample.pdf")
    print(f"Extracted {len(text)} characters from {text.count('--- Page')}")
    print(text[:500])  # show first 500 chars
