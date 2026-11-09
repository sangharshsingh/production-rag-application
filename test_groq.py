
import os
from dotenv import load_dotenv
from groq import Groq

print("Starting Groq test...", flush=True)

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    raise ValueError("Groq API key missing!")

print("API key detected.", flush=True)

client = Groq(
    api_key=api_key,
    timeout=20.0,
    max_retries=0
)

print("Sending request to Groq...", flush=True)

try:
    response = client.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=[
            {"role": "user", "content": "Say hello in one sentence."}
        ],
        max_completion_tokens=100
    )

    print("SUCCESS!", flush=True)
    print(response.choices[0].message.content)

except Exception as e:
    print("Groq request failed:", type(e).__name__, str(e))
