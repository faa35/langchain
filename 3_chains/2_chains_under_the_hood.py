from dotenv import load_dotenv
from langchain.prompts import ChatPromptTemplate
from langchain.schema.runnable import RunnableLambda, RunnableSequence
# from langchain_openai import ChatOpenAI
from langchain_google_genai import GoogleGenerativeAI
from pydantic import SecretStr
import os

# Load environment variables from .env
load_dotenv()

# Create a ChatOpenAI model
# model = ChatOpenAI(model="gpt-4")

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

# Define prompt templates
prompt_template = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a comedian who tells jokes about {topic}."),
        ("human", "Tell me {joke_count} jokes."),
    ]
)

# Create individual runnables (steps in the chain)
format_prompt = RunnableLambda(lambda x: prompt_template.format_prompt(**x))
invoke_model = RunnableLambda(lambda x: model.invoke(x.to_messages())) # to_messages() shows problem because of GoogleGenerativeAI
parse_output = RunnableLambda(lambda x: x)

# Create the RunnableSequence (equivalent to the LCEL chain)
chain = RunnableSequence(first=format_prompt, middle=[invoke_model], last=parse_output)

# Run the chain
response = chain.invoke({"topic": "lawyers", "joke_count": 3})

# Output
print(response)
