
import os

from twitter.account import Account

cookie_path = os.path.join(os.curdir, 'twitter.cookies')
account = Account(cookies=cookie_path)


def upload_tweet(answer: str, image_path: str, dalle_prompt: str) -> str:
    response = account.tweet(answer, media=[
        {'media': image_path, 'alt': dalle_prompt},
    ])
    return response['data']['create_tweet']['tweet_results']['result']['legacy']['entities']['media'][0]['url']
