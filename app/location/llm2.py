from gradio_client import Client, file

from app.core.config import CONFIG

from typing import Tuple
import json

_client = Client("Qwen/Qwen3-Demo", HF_TOKEN = CONFIG.HF_TOKEN)

def _get_landmarks_prompt(location : str, article : str):
    with open("app/location/prompt_get_landmarks.llm", "r") as f:
        prompt = f.read()
    prompt = prompt.replace("{{location}}", location)
    prompt = prompt.replace("{{article}}", article)
    return prompt

def get_landmarks(location : str, wiki_page : str) -> str:
    result = _client.predict(
        input_value=_get_landmarks_prompt(location, wiki_page),
        settings_form_value = {
            "model":"qwen3-30b-a3b",
            "thinking_budget":38
        },
        api_name="/add_message"
    )
    resp = response.choices[0].message.content
    jResp = json.loads(resp)
