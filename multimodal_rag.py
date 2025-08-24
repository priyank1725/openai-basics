import os
import base64
from io import BytesIO
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.schema import HumanMessage
from PIL import Image

load_dotenv()

# --- Multimodal model ---
llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",  # "pro" supports vision
    google_api_key=os.getenv("GOOGLE_API_KEY")
)

def ask_with_image(image_path, question):
    img = Image.open(image_path)
    print(img)
    
    # Convert PIL image to base64
    buffered = BytesIO()
    img.save(buffered, format="JPEG")
    img_str = base64.b64encode(buffered.getvalue()).decode()
    
    # Create message with both image and text
    message = HumanMessage(content=[
        {"type": "text", "text": question},
        {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{img_str}"}}
    ])
    
    response = llm.invoke([message])
    return response.content

if __name__ == "__main__":
    print("🤖 Multimodal Q&A Demo")
    answer = ask_with_image("receipt.jpg", "who is biller")
    print("\nAI:", answer)
