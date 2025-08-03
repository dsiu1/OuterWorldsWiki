import base64
import io
import os
import time
from pathlib import Path

import pandas as pd
import requests
from dotenv import load_dotenv
from PIL import Image

from prompts import log_prompt, terminal_prompt
from utils import create_prompt, group_images

# OpenAI API Key
load_dotenv()
OPENAI_KEY = os.environ.get("OPENAI_API_KEY")
OPENAI_REQUEST = "https://api.openai.com/v1/chat/completions"
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {OPENAI_KEY}",
}


def run_pipeline(prompt, items, file_name, n_lim: int = 0):
    data = []
    # Getting the base64 string
    for n, (k, v) in enumerate(items.items()):
        if n < n_lim:
            continue
        payload = create_prompt(prompt, v)
        response = requests.post(
            OPENAI_REQUEST,
            headers=headers,
            json=payload,
        )
        output = response.json()
        try:
            text = output["choices"][0]["message"]["content"]
        except KeyError:
            print("Rate limit exceeded. Waiting for 60 seconds...")
            time.sleep(60)
            response = requests.post(
                OPENAI_REQUEST,
                headers=headers,
                json=payload,
            )
            output = response.json()
            text = output["choices"][0]["message"]["content"]

        data.append(
            {
                "text": text,
                "name": k,
                "tokens": output["usage"]["total_tokens"],
            },
        )
        print(f"Processed {k} with {len(v)} images")
        print(text)
        df = pd.DataFrame(data)
        df.to_csv(f"{file_name}.csv", index=False)

    return data


if __name__ == "__main__":
    # Path to your image. We expect it to be nested in this format
    # OuterWorlds
    #     - Logs
    #         - Logs1_Img.jpg
    #         - Logs1_1.jpg
    #     - Terminals
    #         - Terminal1_1.jpg
    #         - Terminal1_2.jpg
    image_folder = "E:\\Projects\\OuterWordsPicST\\"
    project = "Terminals"
    image_list = [Path(image_folder, project, i) for i in Path(image_folder, project).iterdir()]
    image_list = [
        i
        for i in image_list
        if not i.name.startswith(".") and i.name.startswith("R&D_Lab_Terminal_")
    ]
    terminals = group_images(image_list)
    print(image_list)

    project = "Logs"
    image_list = [Path(image_folder, project, i) for i in Path(image_folder, project).iterdir()]
    image_list = [i for i in image_list if not i.name.startswith(".")]
    logs = group_images(image_list[0:2])

    # run_pipeline(log_prompt, logs, "log", n_lim=0)
    run_pipeline(terminal_prompt, terminals, "terminal", n_lim=0)
