from dotenv import load_dotenv
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
from langchain_google_genai import GoogleGenerativeAI
from pydantic import SecretStr
import os

# Load environment variables from .env
load_dotenv()

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

# SystemMessage:
#   Message for priming AI behavior, usually passed in as the first of a sequenc of input messages.
# HumanMessagse:
#   Message from a human to the AI model.
messages = [
    SystemMessage(content="Solve the following math problems"),
    HumanMessage(content="What is 81 divided by 9?"),
]

# Invoke the model with messages
result = model.invoke(messages)
print(f"Answer from AI: {result}")




#       ***comment out this part for a full blown conversation***

# # AIMessage:
# #   Message from an AI.
# messages = [
#     SystemMessage(content="Solve the following math problems"),
#     HumanMessage(content="What is 81 divided by 9?"),
#     AIMessage(content="81 divided by 9 is 9."),
#     HumanMessage(content="What is 10 times 5?"),
# ]

# # Invoke the model with messages
# result = model.invoke(messages)
# print(f"Answer from AI: {result}")
