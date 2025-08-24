import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain

# Load environment variables
load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

# Initialize Gemini model via LangChain
llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", google_api_key=api_key)

# Memory: stores conversation history
memory = ConversationBufferMemory()

# Build conversation chain
conversation = ConversationChain(
    llm=llm,
    memory=memory,
    # verbose=True  # shows intermediate steps
)

# Simple chat loop
print("🤖 Chatbot is ready! Type 'exit' to quit.\n")
while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit"]:
        print("👋 Goodbye!")
        break
    response = conversation.predict(input=user_input)
    print(f"AI: {response}\n")
