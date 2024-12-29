from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAI
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage

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


chat_history = []  # Use a list to store messages

# Set an initial system message (optional)
system_message = SystemMessage(content="You are a helpful AI assistant.")
chat_history.append(system_message)  # Add system message to chat history

# Chat loop
while True:
    query = input("You: ")           # Prompt the user for input
    if query.lower() == "exit":      # Exit the loop if the user types "exit"
        break
    chat_history.append(HumanMessage(content=query))        # Add the user's message to the chat history

    # Get AI response using history
    result = model.invoke(chat_history)                     # Call the AI model with the current chat history
    response = result                                       # Store the AI's response
    chat_history.append(AIMessage(content=response))        # Add the AI's response to the chat history

    print(f"AI: {response}")                    # Print the AI's response to the console

# After exiting the loop, print the entire chat history
print("---- Message History ----")              # Print a header for the message history
print(chat_history)                             # Display the full chat history including system, user, and AI messages
