# chatbot.py — PDF chatbot using Gemini
import os
from dotenv import load_dotenv
from google import genai
from extract import extract_text
from chunk import chunk_text

load_dotenv()

client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])

# --- Build the knowledge base once ---
def build_knowledge_base(pdf_path):
    text = extract_text(pdf_path)
    chunks = chunk_text(text)
    return chunks

KB = build_knowledge_base("sample.pdf")

SYSTEM_PROMPT = """You are a helpful study assistant.
Answer questions using ONLY the provided document excerpts.
If the answer isn't in the excerpts, say so clearly.
Always cite which page the information came from."""

def ask(question, kb):
    context = "\n\n".join(kb)

    response = client.models.generate_content(
        model="gemini-3.8-flash",
        contents=f"{SYSTEM_PROMPT}\n\nDocument:\n{context}\n\nQuestion: {question}",
        config={
            "temperature": 0.0,  # deterministic
        }
    )
    return response.text

# --- The chat loop ---
print("PDF Chatbot ready. Type 'quit' to exit.")
while True:
    question = input("\nYou: ").strip()
    if question.lower() in ("quit", "exit", "q"):
        print("Goodbye!")
        break
    if not question:
        continue
    print("Thinking...")
    answer = ask(question, KB)
    print(f"Bot: {answer}")


