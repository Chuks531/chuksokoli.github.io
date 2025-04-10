import subprocess,sys
from fastapi import FastAPI, UploadFile, File
import openai
from google.cloud import speech, texttospeech

packages = [
    "fastapi",
    "uvicorn",
    "openai",
    "google-cloud-speech",
    "google-cloud-texttospeech"
]

subprocess.check_call([sys.executable, "-m", "pip", "install"] + packages)

app = FastAPI()

# OpenAI API Key (Set as ENV variable)
openai.api_key = "your-openai-api-key"

# Initialize Google Speech and Text-to-Speech Clients
speech_client = speech.SpeechClient()
tts_client = texttospeech.TextToSpeechClient()

@app.post("/transcribe/")
async def transcribe_audio(file: UploadFile = File(...)):
    content = await file.read()
    audio = speech.RecognitionAudio(content=content)
    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=16000,
        language_code="en-US",
    )
    response = speech_client.recognize(config=config, audio=audio)
    transcription = response.results[0].alternatives[0].transcript
    return {"transcription": transcription}