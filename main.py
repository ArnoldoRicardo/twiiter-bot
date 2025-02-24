import random

from dotenv import load_dotenv

from openai_resource import generate_chat_message, generate_image
from twitter_bot import upload_tweet
from utils import clean_up, save_image

load_dotenv()


def select_character(characters: list) -> dict:
    return random.choice(characters)


def main():
    characters = [
        {
            "name": "nina",
            "description": "black cat with yellow eyes",
        },
        {
            "name": "cutie",
            "description": "Gray tabby cat",
        },
        {
            "name": "chingueki",
            "description": "Dark cat, with belly white hair",
        },
        {
            "name": "petra",
            "description": "Blue Merle dog with chest white hair",
        },
        {
            "name": "mayoneso",
            "description": "orange tabby cat",
        },
        {
            "name": 'travel',
            "description": "this is a random image of a place",
        }
    ]

    character = select_character(characters)

    message = [
        {
            "role": "system",
            "content": "You are a helpful assistant that helps to a short paragraph history of the character."
        },
        {
            "role": "user",
            "content": """{name} is {description}. be creative and add some details.
            """.format(
                name=character['name'],
                description=character['description'],
            )
        }
    ]

    short_history = generate_chat_message(message)
    print('short_history: ', short_history)

    messages = [
        {
            "role": "system",
            "content": """Your task is to refine and enhance any DALL·E prompt you receive.
            Add more details to improve the visual quality and ensure that the final image
            is well-defined and visually appealing. Always preserve the pixel art style,
            emphasizing elements like shading, depth, color contrast, and retro aesthetics."""
        },
        {
            "role": "user",
            "content": short_history
        },
    ]

    dalle_prompt = generate_chat_message(messages)
    print('dalle_prompt: ', dalle_prompt)

    image_url = generate_image(dalle_prompt)
    image_path = save_image(image_url)

    messages = [
        {
            "role": "system",
            "content": """You will receive descriptions of pixel art pieces intended for DALL·E 3.
            Your task is to transform these prompts into engaging, visually evocative,
            and concise tweets that capture the essence of the artwork while making them
            more appealing for a broad audience. limit the tweet to 60 characters."""
        },
        {
            "role": "user",
            "content": dalle_prompt
        },
    ]

    answer = generate_chat_message(messages)
    print('answer: ', answer)

    tweet_url = upload_tweet(answer, image_path, dalle_prompt)
    print(tweet_url)

    # Clean up
    clean_up(image_path)


if __name__ == "__main__":
    main()
