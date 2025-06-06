import pyttsx3
import numpy as np
import cv2
import wave
import struct
import time
import os
import matplotlib.pyplot as plt
from playsound import playsound

# Defining the Functions

def draw_avatar(mouth_open=False):
    """Draws an avatar with an open or closed mouth."""
    img = np.zeros((400, 400, 3), dtype="uint8")  # Black background
    cv2.circle(img, (200, 150), 80, (255, 255, 255), -1)  # Head
    cv2.circle(img, (170, 130), 10, (0, 0, 0), -1)  # Left Eye
    cv2.circle(img, (230, 130), 10, (0, 0, 0), -1)  # Right Eye

    mouth_color = (0, 0, 255)  # Red mouth
    if mouth_open:
        cv2.ellipse(img, (200, 200), (40, 30), 0, 0, 360, mouth_color, -1)  # Open mouth
    else:
        cv2.ellipse(img, (200, 200), (40, 10), 0, 0, 360, mouth_color, -1)  # Closed mouth

    return img

def get_audio_frames(audio_file):
    """Extracts volume levels from an audio file for lip-sync animation."""
    with wave.open(audio_file, "rb") as wf:
        frames = wf.readframes(wf.getnframes())
        frame_count = wf.getnframes()
        frame_rate = wf.getframerate()
        audio_duration = frame_count / frame_rate

        # Convert unpacked audio data to a list of integers
        audio_data = list(struct.unpack("<" + str(frame_count) + "h", frames))
        
        chunk_size = int(frame_rate / 10)  # 10 chunks per second
        volume_levels = [sum(abs(x) for x in audio_data[i : i + chunk_size]) for i in range(0, len(audio_data), chunk_size)]
        
        return volume_levels, audio_duration

# Main Executions

# Initialize text-to-speech engine
engine = pyttsx3.init()
engine.setProperty('rate', 150)  # Speed of speech
engine.setProperty('volume', 1.0)  # Volume level

# Welcome message
message = """
Welcome to New Revelation Baptist Church (NRBC)!  
A place where God is actively molding lives for greatness through Christ! We are delighted to have you with us, and on behalf of our Lead Pastor, Rev. Darlington Amadi, his wife, Pastor Mrs. Amadi, the Pastorate, the Diaconate, and the entire NRBC family, we warmly welcome you to experience God’s presence like never before.

Weekly Activities - Join Us & Be Transformed!  
Tuesdays | Hour of Grace (6:00 PM - 7:00 PM)  
A sacred time of prayer and reflection, come with open hearts as we seek God, lift our requests, and grow deeper in His presence."


Wednesdays | Midweek Service (6:00 PM - 7:30 PM)  
A powerful time of prayer, worship, and undiluted teachings to recharge your faith!

Sundays | Worship Experience  
- Sunday School (8:30 AM - 9:25 AM) → A time to explore the depths of the Bible and its timeless truths.  
- Celebration Service (9:30 AM - 11:30 AM) → Join us for a powerful time of praise, worship, and a life-transforming Word from God’s servant.  

We can't wait to see you grow, connect, and flourish in Christ!   
New Revelation Baptist Church is a model Church committed to Molding Lives for Greatness in Christ. 
"""

# Save speech to file
audio_file = "welcome_message.wav"
engine.save_to_file(message, audio_file)
engine.runAndWait()

# Save the text to a file
text_file = "transcription.txt"
with open(text_file, "w", encoding="utf-8") as file:
    file.write(message)
print(f"Transcription saved to: {text_file}")

# Get volume levels for avatar animation
volume_levels, duration = get_audio_frames(audio_file)

# Play audio and animate avatar
playsound(audio_file)

start_time = time.time()
for vol in volume_levels:
    elapsed_time = time.time() - start_time
    if elapsed_time >= duration:
        break  # Stop animation when audio ends

    mouth_open = vol > max(volume_levels) * 0.4  # Open mouth if volume is high
    avatar = draw_avatar(mouth_open)
    cv2.imshow("Talking Avatar", avatar)
    cv2.waitKey(100)

cv2.destroyAllWindows()
print("Avatar animation complete!")
print(f"audio_file: {audio_file}")
