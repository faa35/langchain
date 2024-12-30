from dotenv import load_dotenv
from langchain.prompts import ChatPromptTemplate
from langchain.schema.output_parser import StrOutputParser
# from langchain_openai import ChatOpenAI
from langchain_google_genai import GoogleGenerativeAI
from pydantic import SecretStr
#The api_key is fetched from environment variables. If it's not set, an error is raised.
import os

# Load environment variables from .env
load_dotenv()

# # Create a ChatOpenAI model
# model = ChatOpenAI(model="gpt-4o")

# Convert API key to SecretStr
api_key = os.getenv("GOOGLE_API_KEY")
if api_key is None:
    raise ValueError("GOOGLE_API_KEY is not set in the environment variables.")
    
secret_api_key = SecretStr(api_key)

# Create a ChatOpenAI model
model = GoogleGenerativeAI(
    model="gemini-1.5-pro",
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2,
    api_key=secret_api_key  # Use SecretStr
)

# Define prompt templates (no need for separate Runnable chains)

# messages = [
#         ("system", "You are a comedian who tells jokes about {topic}."),
#         ("human", "Tell me {joke_count} jokes."),
# ]
# prompt_template = ChatPromptTemplate.from_messages(messages)

#reducing one step
prompt_template = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a comedian who tells jokes about {topic}."),
        ("human", "Tell me {joke_count} jokes."),
    ]
)

# Create the combined chain using LangChain Expression Language (LCEL)

#lets first do it witout the output parser
chain = prompt_template | model

# chain = prompt_template | model | StrOutputParser()
# doesnt make any difference because its GoogleGenerativeAI not ChatOpenAI


# Run the chain
result = chain.invoke({"topic": "lawyers", "joke_count": 3})

# Output
print(result)
