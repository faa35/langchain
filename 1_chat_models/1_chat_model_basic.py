# Chat Model Documents: https://python.langchain.com/v0.2/docs/integrations/chat/
# OpenAI Chat Model Documents: https://python.langchain.com/v0.2/docs/integr
from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAI
from pydantic import SecretStr
#The api_key is fetched from environment variables. If it's not set, an error is raised.
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

# Invoke the model with a message
result = model.invoke("What is 81 divided by 9?")
print("Full result:")
print(result)

# i think this doesnt work anymore or doesnt work with gogglegeneratveai
# print("Content only:")
# print(result.content)