import base64
import io
from pathlib import Path

from PIL import Image


def group_images(image_list: list[Path]) -> dict:
    """Group images by their common prefix."""
    grouped_images = {}
    for image_path in image_list:
        # Extract the prefix (Everything except the last number)
        # For example: OuterWorlds/Logs/image_test_test2_1.jpg -> image_test_test2
        prefix = image_path.stem.rsplit("_", 1)[0]
        suffix = image_path.stem.rsplit("_", 1)[-1]
        if prefix not in grouped_images:
            grouped_images[prefix] = []
        try:
            int(suffix)
        except ValueError:
            continue
        grouped_images[prefix].append(image_path)
    return grouped_images


# Function to encode the image
def encode_image(image_path) -> str:
    """1. Read the image file and downsample it to 1280x720
    2. Convert the image to base64 string
    """
    # Open the image using Pillow
    img = Image.open(image_path)

    # Resize the image
    resized_img = img.resize((1280, 720))

    # Create an in-memory byte stream
    img_byte_arr = io.BytesIO()

    # Save the resized image to the byte stream in the specified format
    resized_img.save(img_byte_arr, format="JPEG", quality=85)

    # Get the byte data from the stream
    img_byte_arr = img_byte_arr.getvalue()

    # Encode the bytes to base64
    return base64.b64encode(img_byte_arr).decode("utf-8")


def make_image_prompt(image_list: list) -> list:
    """Given all of the images, then create the prompt for the images."""
    if isinstance(image_list, str):
        image_list = [image_list]

    image_prompt = []
    for i in image_list:
        base64_image = encode_image(i)
        prompt_base = {
            "type": "image_url",
            "image_url": {
                "url": f"data:image/jpeg;base64,{base64_image}",
            },
        }

        image_prompt.append(prompt_base)
    return image_prompt


def create_prompt(text_prompt: str, image_list: list[str]) -> dict:
    """Process log or terminal images, given the input prompt."""
    image_prompt = make_image_prompt(image_list)
    return {
        "model": "gpt-4o",
        "messages": [
            {
                "role": "user",
                "content": [  # noqa: RUF005
                    {
                        "type": "text",
                        "text": text_prompt,
                    },
                ]
                + image_prompt,
            },
        ],
        "max_tokens": 3000,
    }
