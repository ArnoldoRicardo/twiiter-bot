import os

from dotenv import load_dotenv
from openai import AzureOpenAI

load_dotenv()

client = AzureOpenAI(
    api_version="2024-05-01-preview",
    azure_endpoint=os.environ["ENDPOINT_URL"],
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
)


def generate_image(prompt: str) -> str:
    result = client.images.generate(
        model="dall-e-3",
        prompt=prompt,
        n=1
    )
    return result.data[0].url


def generate_chat_message(messages: list) -> str:
    result = client.chat.completions.create(
        model="gpt-35-turbo",
        messages=messages,
        max_tokens=800,
        temperature=0.7,
        top_p=0.95,
        frequency_penalty=0,
        presence_penalty=0
    )
    return result.choices[0].message.content
