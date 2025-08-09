import os
from dotenv import load_dotenv
from google import genai
import sys
from google.genai import types

# Load environment variables
load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

if len(sys.argv) < 2:
    print("Error: No prompt given.\nUsage: python main.py <your prompt here>")
    sys.exit(1)
prompt = sys.argv[1]
verbose = "--verbose" in sys.argv[2:]

# Create client
client = genai.Client(api_key=api_key)

# Generate content
response = client.models.generate_content(
    model="gemini-2.0-flash-001",
    contents=prompt
)

# Print the response
print(response.text)

# Print if verbose included
if verbose:
    print(f"User prompt: {prompt}")
    print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
    print(f"Response tokens: {response.usage_metadata.candidates_token_count}")

# List of past messages
messages = [
    types.Content(role="user", parts=[types.Part(text=prompt)]),
]

