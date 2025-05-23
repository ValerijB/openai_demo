import os
from openai import OpenAI
from dotenv import load_dotenv
from my_openai import init_openai_client
from my_openai import start_chat

load_dotenv()  # Load environment variables from .env file
# Load your OpenAI API key from an environment variable or directly
# from .env file

    

# 1. Setup OpenAI client (Insert your API key here or use environment variable)
token = os.getenv("SECRET")  # Replace with your actual token
endpoint = "https://models.github.ai/inference"
model = "openai/gpt-4.1-nano"

# initialize the OpenAI client
# Note: The OpenAI client is initialized with the base URL and API key.
client = init_openai_client(token, endpoint)
messages = start_chat()

# 3. Ask a question
question = "What is Biržai famous for?"

while True:
    user_input = input( )

    if user_input == 'exit':
        print("Ačiū, iki greito pasimatymo!")
        exit()

    # Add user message to history
    messages.append(
        {"role": "user", "content": user_input})

    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=0.7,
        top_p=1.0,
        max_tokens=300
    )

    reply = response.choices[0].message.content
    # Add assistant reply to history
    messages.append({"role": "assistant", "content": reply})
    print(reply)

