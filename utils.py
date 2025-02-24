
import os
import httpx
import re
import shutil

image_dir = os.path.join(os.curdir, 'images')


def save_image(image_url: str):
    uuid_pattern = re.compile(r'[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}')
    match = uuid_pattern.search(image_url)
    image_path = os.path.join(image_dir, f'generated_image_{match.group()}.png')
    generated_image = httpx.get(image_url).content  # download the image
    with open(image_path, "wb") as image_file:
        image_file.write(generated_image)

    return image_path


def clean_up(image_path: str):
    destination = f'{image_dir}/done/'
    shutil.move(image_path, destination)


def create_if_dont_exists(dir: str):
    if not os.path.isdir(dir):
        os.mkdir(dir)


create_if_dont_exists(image_dir)
create_if_dont_exists(f'{image_dir}/done')
