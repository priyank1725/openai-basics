import os
import google.generativeai as genai
from dotenv import load_dotenv
import json

# Load API key
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel("gemini-1.5-flash")

# Prompt to force JSON format
prompt = """
Extract information in JSON format.

Do not add any text outside JSON. No explanations, no markdown.

Text: "JavaScript is used for frontend, backend, and game development."

Return JSON with keys:
- language
- use_cases (list)

retrun only stringified JSON, no other text.
"""

response = model.generate_content(prompt)

text = response.text.replace("```json", "").replace("```", "")

print("\n🤖 Raw AI Response:")
print(response.text)
print(text)

# Try parsing into JSON
try:
    parsed = json.loads(text)
    print("\n✅ Parsed JSON:")
    print(parsed)
except Exception as e:
    print("\n⚠️ Failed to parse JSON:", e)
