import os
import random
import re
import shutil

import openai
from dotenv import load_dotenv
from twitter.account import Account

load_dotenv()

current_file_path = os.path.abspath(__file__)

current_directory = os.path.dirname(current_file_path)
directory = os.path.join(current_directory, 'photos')

jpg_files = [f for f in os.listdir(directory) if f.endswith('.png')]

random_file = random.choice(jpg_files)

full_path = os.path.join(directory, random_file)

pattern = r'- (.+?)\.png'

matches = re.findall(pattern, random_file)

dalle_prompt = " ".join(matches)

messages = [
    {"role": "system",
     "content": "You will be provided with descriptions of pixel art pieces. Your task is to turn these descriptions into attractive and creative short tweets."},
    {"role": "user", "content": dalle_prompt},
]

openai.organization = os.environ.get("ORG")
openai.api_key = os.environ.get("API_KEY")

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=messages,
    temperature=0.7,
    max_tokens=256
)

answer = response['choices'][0]['message']['content']

cookie_path = os.path.join(current_directory, 'twitter.cookies')
account = Account(cookies=cookie_path)

response = account.tweet(answer, media=[
    {'media': full_path, 'alt': dalle_prompt},
])

print(f"Prompt: {dalle_prompt}")
print(f"Media: {random_file}")
print(f"Respuesta: {answer}")
print(response['data']['create_tweet']['tweet_results']['result']['legacy']['entities']['media'][0]['url'])

# Clean up
destination = f'{directory}/done/'
shutil.move(full_path, destination)
