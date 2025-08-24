import os
from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAIEmbeddings, ChatGoogleGenerativeAI
from langchain_community.vectorstores import Chroma
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains import RetrievalQA
from langchain_community.document_loaders import TextLoader

load_dotenv()

# --- LLM and Embeddings ---
llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", google_api_key=os.getenv("GOOGLE_API_KEY"))
embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001", google_api_key=os.getenv("GOOGLE_API_KEY"))

# --- Load and split a text file ---
loader = TextLoader("data.txt")  # <- create a text file named data.txt
docs = loader.load()
splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)
chunks = splitter.split_documents(docs)

# --- Store chunks in Chroma ---
db = Chroma.from_documents(chunks, embeddings, persist_directory="chroma_db")

# --- Create retriever + QA chain ---
retriever = db.as_retriever(search_kwargs={"k": 3})
qa_chain = RetrievalQA.from_chain_type(llm=llm, retriever=retriever, return_source_documents=True)

# --- Ask questions ---
while True:
    q = input("\nAsk: ")
    if q.lower() in ("exit", "quit"):
        break
    result = qa_chain({"query": q})
    print("\nAI:", result["result"])
    print("Sources:", [doc.metadata.get("source") for doc in result["source_documents"]])
