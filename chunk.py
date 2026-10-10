
# chunk.py — break text into pieces the model can work with
from extract import extract_text

def chunk_text(text, chunk_size=800, overlap=100):
    """Split text into overlapping chunks."""
    chunks = []
    start = 0
    while start < len(text):
        end = start + chunk_size
        chunk = text[start:end]
        chunks.append(chunk)
        # move forward, but keep 'overlap' chars for context
        start = end - overlap
        if end >= len(text):
            break
    return chunks

if __name__ == "__main__":
    text = extract_text("sample.pdf")
    chunks = chunk_text(text)
    print(f"Split into {len(chunks)} chunks")
    for i, chunk in enumerate(chunks[:3]):
        print(f"\n--- Chunk {i+1} ({len(chunk)} chars) ---")
        print(chunk[:200])