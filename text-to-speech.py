from PIL import Image
import pytesseract
import pyttsx3

# Step 1: Load the image (Fixed Path)
image_path = r"C:\Users\Chuks\Pictures\Image.jpg"  # Corrected file path
image = Image.open(image_path)

# Step 2: Perform OCR to extract text
extracted_text = pytesseract.image_to_string(image)

# Step 3: Initialize the text-to-speech engine
engine = pyttsx3.init()

# Set speech properties (optional)
engine.setProperty('rate', 150)  # Speed of speech
engine.setProperty('volume', 1.0)  # Volume level

# Step 4: Convert text to speech and save as an audio file
output_audio_path = "output_audio.mp3"
engine.save_to_file(extracted_text, output_audio_path)
engine.runAndWait()

print(f"Speech saved as {output_audio_path}")
