import os
from openai import OpenAI


# initialize the OpenAI client
# Note: The OpenAI client is initialized with the base URL and API key.
def init_openai_client(token, endpoint):
    """
    Initialize the OpenAI client with the provided endpoint and token.
    """
    # Check if the token is set
    if not token:
        raise ValueError("API key (SECRET) is not set in the environment variables.")
    
    # Check if the endpoint is set
    if not endpoint:
        raise ValueError("Endpoint is not set in the environment variables.")
    
    # Initialize the OpenAI client
    return OpenAI(
        base_url=endpoint,
        api_key=token,
    )

# Load context from a text file.
def load_context(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return file.read()
    except FileNotFoundError:
        print(f"❌ {file_path} not found.")
        return None

def start_chat():
    """
    Start a chat session with the OpenAI client.
    """
    print("Esu asistentas, galintis atsakyti į Jūsų klausimus")
    print("Atsakysiu į Jūsu klausimus lietuvių kalba")
    print("Norėdamas išeiti rašykyte 'exit' \n")
    
    print("Užduokite savo klausimą: ")

    messages = [
        {"role": "system", "content": "You are a helpful assistant. You always answer in Lithuanian. Please remember our conversation.",
        },
        {"role": "user", "content": f"Context: {load_context('birzai.txt')}\n\n"}
    ]
    
    return messages