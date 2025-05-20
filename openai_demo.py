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

print("Esu asistentas, galintis atsakyti į Jūsų klausimus\n")
 print("AI Bot (rašyk 'exit' norėdamas išeiti)\n")

while True:
    user_input = input("Užduokite savo klausimą: ")

    if user_input == 'exit':
        print("Ačiū, iki greito pasimatymo!")
        exit()

    response = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": "You are a helpful assistant. You always answer in Lithuanian",
            },
            {
                "role": "user",
                "content": f'{user_input}',
            }
        ],
        temperature=1.0,
        top_p=1.0,
        model=model
    )

    print(response.choices[0].message.content)