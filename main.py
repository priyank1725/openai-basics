import os
import sys
import google.generativeai as genai # type: ignore
from dotenv import load_dotenv

# load .env
load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

# configure Gemini
genai.configure(api_key=api_key)

# set default model
model = genai.GenerativeModel("gemini-1.5-flash")

# take prompt from CLI or default
prompt = sys.argv[1] if len(sys.argv) > 1 else "Hello AI, explain recursion in simple terms."

# generate response
response = model.generate_content(prompt)

print("\n🤖 AI Response:")
print(response.text)
