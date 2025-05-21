import os
from openai import OpenAI

from dotenv import load_dotenv

load_dotenv()  # take environment variables

# from .env file
# Load environment variables from .env file

token = os.getenv("SECRET")  # Replace with your actual token
endpoint = "https://models.github.ai/inference"
model = "openai/gpt-4.1-nano"

# initialize the OpenAI client
# Note: The OpenAI client is initialized with the base URL and API key.
client = OpenAI(
    base_url=endpoint,
    api_key=token,
)

print("Esu asistentas, galintis atsakyti į Jūsų klausimus")
print("Atsakysiu į Jūsu klausimus lietuvių kalba")
print("Norėdamas išeiti rašykyte 'exit' \n")

print("Užduokite savo klausimą: ")


messages = [
    {
        "role": "system",
        "content": "You are a helpful assistant. You always answer in Lithuanian. Please remember our conversation.",
    }
]

while True:
    user_input = input( )

    if user_input == 'exit':
        print("Ačiū, iki greito pasimatymo!")
        exit()

    # Add user message to history
    messages.append({"role": "user", "content": user_input})

    response = client.chat.completions.create(
        messages=messages,
        temperature=1.0,
        top_p=1.0,
        model=model
    )

    reply = response.choices[0].message.content
    # Add assistant reply to history
    messages.append({"role": "assistant", "content": reply})
    print(reply)