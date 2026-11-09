
from dotenv import load_dotenv
from langchain_groq import ChatGroq

# Load API key from .env
load_dotenv()

# Initialize the model
model = ChatGroq(
    model="openai/gpt-oss-20b",
    temperature=0.5
)

# Invoke the model
response = model.invoke("Say hello in one sentence.")

# Print the response
print(response.content)
