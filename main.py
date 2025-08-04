from fastapi import FastAPI
from pydantic import BaseModel
import requests

app = FastAPI()

class TextInput(BaseModel):
    text: str

@app.post("/generate-audio")
def generate_audio(input: TextInput):
    # Replace with your actual Murf TTS API key
    murf_api_key = "ap2_d5d04dfc-c299-4cd1-9702-0cee60d680ab"

    murf_endpoint = "https://api.murf.ai/v1/speech/generate"

    payload = {
        "text": input.text,
        "voice": "en-US-Wavenet-D"  # Example voice
    }

    headers = {
        "Authorization": f"Bearer {murf_api_key}",
        "Content-Type": "application/json"
    }

    response = requests.post(murf_endpoint, json=payload, headers=headers)

    if response.status_code == 200:
        result = response.json()
        return {"audio_url": result.get("audio_url")}
    else:
        return {"error": "Failed to generate audio", "details": response.text}
