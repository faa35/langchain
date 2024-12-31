# UNFORTUNATELY, THE GOOGLE GENERATIVE AI MODEL IS NOT WORKING AS EXPECTED. 
# Positive, Negative, Neutral Feedback ARE BEING CLASSIFIED AS ESCALATE.(IN CHATGPT IT WORKS FINE)
# Escalate Feedback IS BEING CLASSIFIED AS POSITIVE. (IN CHATGPT IT WORKS FINE)
#SEE THE OUTPUT BELOW


from dotenv import load_dotenv
from langchain.prompts import ChatPromptTemplate
from langchain.schema.output_parser import StrOutputParser
from langchain.schema.runnable import RunnableBranch
# from langchain_openai import ChatOpenAI
from langchain_google_genai import GoogleGenerativeAI
from pydantic import SecretStr
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


# Define prompt templates for different feedback types
positive_feedback_template = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant."),
        ("human",
         "Generate a thank you note for this positive feedback: {feedback}."),
    ]
)

negative_feedback_template = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant."),
        ("human",
         "Generate a response addressing this negative feedback: {feedback}."),
    ]
)

neutral_feedback_template = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant."),
        (
            "human",
            "Generate a request for more details for this neutral feedback: {feedback}.",
        ),
    ]
)

escalate_feedback_template = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant."),
        (
            "human",
            "Generate a message to escalate this feedback to a human agent: {feedback}.",
        ),
    ]
)

# Define the feedback classification template
classification_template = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant."),
        ("human",
         "Classify the sentiment of this feedback as positive, negative, neutral, or escalate: {feedback}."),
    ]
)

# Define the runnable branches for handling feedback
branches = RunnableBranch(
    (
        lambda x: "positive" in x,
        positive_feedback_template | model | StrOutputParser()  # Positive feedback chain
    ),
    (
        lambda x: "negative" in x,
        negative_feedback_template | model | StrOutputParser()  # Negative feedback chain
    ),
    (
        lambda x: "neutral" in x,
        neutral_feedback_template | model | StrOutputParser()  # Neutral feedback chain
    ),
    escalate_feedback_template | model | StrOutputParser()
)

# Create the classification chain
classification_chain = classification_template | model | StrOutputParser()

# Combine classification and response generation into one chain
chain = classification_chain | branches



# Run the chain with an example review
# Good review - "The product is excellent. I really enjoyed using it and found it very helpful."
# ---------> This positive feedback needs a human touch!  A customer shared the following and I think it would be valuable for the team to see: [Insert the positive feedback here].  Could a human agent please review and potentially share this with the relevant team/individual for recognition and encouragement?

# Bad review - "The product is terrible. It broke after just one use and the quality is very poor."
# ---------> "I'm having a negative experience and require assistance from a human agent. Please escalate this feedback."

# Neutral review - "The product is okay. It works as expected but nothing exceptional."
# ---------> "This feedback requires review by a human agent."

# Default - "I'm not sure about the product yet. Can you tell me more about its features and benefits?"
# ---------> Subject: Thank you for your feedback!
# We appreciate you taking the time to provide feedback. We understand your response was neutral, and we interpret this as a potential need for more information about the product.  We'd love to help clarify anything that might be unclear.
# Could you please tell us more about what information you're looking for?  Knowing this will help us improve our product communication and ensure everyone has the details they need.
# Thanks again for your input!

review = "The product is excellent. I really enjoyed using it and found it very helpful."
result = chain.invoke({"feedback": review})

# Output the result
print(result)
