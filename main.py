from dotenv import load_dotenv

from openai_resource import generate_chat_message, generate_image
from twitter_bot import upload_tweet
from utils import clean_up, save_image

load_dotenv()


def main():
    dalle_prompt = "black cat with yellow eyes, jumping the fence, in frances. pixel art style"

    image_url = generate_image(dalle_prompt)
    image_path = save_image(image_url)

    messages = [
        {"role": "system",
         "content": "You will be provided with descriptions of pixel art pieces. Your task is to turn these dalle3 prompt into attractive and creative short tweets."},
        {"role": "user", "content": dalle_prompt},
    ]

    answer = generate_chat_message(messages)

    tweet_url = upload_tweet(answer, image_path, dalle_prompt)
    print(tweet_url)

    # Clean up
    clean_up(image_path)


if __name__ == "__main__":
    main()
