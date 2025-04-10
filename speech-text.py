import whisper

# Load Whisper model
model = whisper.load_model("small")

# Define the audio file path (Windows users should use raw strings or double backslashes)
audio_path = r"C:\Users\Chuks\Videos\Music_audio_file.mp4"

# Transcribe audio
transcription = model.transcribe(audio_path, fp16=False)

# Extract text
text_output = transcription["text"]

# Save the transcription to a text file
output_file = r"C:\Users\Chuks\Documents\transcription.txt"
with open(output_file, "w", encoding="utf-8") as file:
    file.write(text_output)

print(f"Transcription saved successfully to: {output_file}")

