import os
import uuid
from elevenlabs import VoiceSettings
from elevenlabs.client import ElevenLabs

ELEVENLABS_API_KEY = ""
client = ElevenLabs(
    api_key=ELEVENLABS_API_KEY,
)

def text_to_speech_file(text: str) -> str:
    #  calling the text_to_speech conversation API with detailed parameters
    response = client.text_to_speech.convert(
        voice_id="pNInz6obpgDQGcfmajgB" ,  #adam pre made voice
        out_format="mp3_22050_32",
        text=text,
        model_id="eleven_turbo_v2_5",  #use the turbo model for low latency
        # optional voice setting that allow you to coustamize the output
        voice_setting=VoiceSettings

    )