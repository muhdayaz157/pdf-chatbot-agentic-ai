
from dotenv import load_dotenv
from google import genai
import os

# .env file load karein
load_dotenv()

# API key read karein
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError(
        "GEMINI_API_KEY .env file se load nahi hui!"
    )

# Gemini client
client = genai.Client(api_key=api_key)

response = client.models.generate_content(
     model="gemini-3.8-flash",
     contents="Explain AI in simple words."
)

print(response.text)
