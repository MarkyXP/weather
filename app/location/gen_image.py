# .\bin\Release\sd-cli.exe --diffusion-model  z_image_turbo-Q3_K.gguf --vae ..\..\ComfyUI\models\vae\ae.sft  --llm ..\..\ComfyUI\models\text_encoders\Qwen3-4B-Instruct-2507-Q4_K_M.gguf -p "A cinematic, melancholic photograph of a solitary hooded figure walking through a sprawling, rain-slicked metropolis at night. The city lights are a chaotic blur of neon orange and cool blue, reflecting on the wet asphalt. The scene evokes a sense of being a single component in a vast machine. Superimposed over the image in a sleek, modern, slightly glitched font is the philosophical quote: 'THE CITY IS A CIRCUIT BOARD, AND I AM A BROKEN TRANSISTOR.' -- moody, atmospheric, profound, dark academic" --cfg-scale 1.0 -v --offload-to-cpu --diffusion-fa -H 1024 -W 512

import wat
from gradio_client import Client

from app.core.config import CONFIG

client = Client("Qwen/Qwen-Image", hf_token=CONFIG.HF_TOKEN)
result = client.predict(
    prompt="Hello!!",
    seed=0,  # 833095444
    randomize_seed=True,
    aspect_ratio="1:1",
    guidance_scale=4,
    num_inference_steps=50,
    prompt_enhance=True,
    api_name="/infer",
)
wat / result
print(result)
