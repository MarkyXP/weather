# https://justine.lol/oneliners/

# chmod +x ./llamafile-0.9.3
# https://docs.litellm.ai/docs/providers/ollama
from typing import Tuple
import json

from litellm import completion

def _get_landmarks_prompt(location : str, article : str):
    with open("app/location/prompt_get_landmarks.llm", "r") as f:
        prompt = f.read()
    prompt = prompt.replace("{{location}}", location)
    prompt = prompt.replace("{{article}}", article)
    return prompt

def get_landmarks(location : str, wiki_page : str) -> str:
    response = completion(
        model="ollama_chat/gpt-oss", 
        messages=[
            {
                "role": "user",
                "content": _get_landmarks_prompt(location, wiki_page)
            }
        ],
        api_base="http://localhost:11434",
        response_format={
            "type": "json_schema",
            "json_schema": {
                "schema": {
                    "type": "object",
                    "properties": {
                        "iconic_landmark_no_1": {
                            "type": "string"
                        }
                    }
                }
            }
        }
    )
    resp = response.choices[0].message.content
    jResp = json.loads(resp)

