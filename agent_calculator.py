import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import initialize_agent, Tool
from langchain.agents import AgentType
from langchain_community.tools import DuckDuckGoSearchRun

load_dotenv()
llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", google_api_key=os.getenv("GOOGLE_API_KEY"))

# --- Define a simple calculator tool ---
def calculator_tool(expression: str) -> str:
    try:
        return str(eval(expression))
    except Exception as e:
        return f"Error: {e}"

tools = [
    Tool(
        name="Calculator",
        func=calculator_tool,
        description="Useful for doing math calculations"
    ),
    # Tool(
    #     name="Search",
    #     func=DuckDuckGoSearchRun().run,
    #     description="Useful for searching current information"
    # )
]

# --- Initialize agent ---
agent = initialize_agent(
    tools,
    llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)

# --- Try queries ---
print(agent.run("What is 12 * 4?"))
print(agent.run("Who is the current Prime Minister of India?"))
