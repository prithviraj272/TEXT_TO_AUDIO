from gtts import gTTS
import os
import sys

def text_to_speech():
    try:
        # Step 1: Take input from user
        text = input("Enter the text you want to convert to audio:\n").strip()

        # Safety Check 1: Empty input
        if not text:
            print("❌ Error: You did not enter any text.")
            return

        # Step 2: Create TTS object
        tts = gTTS(text=text, lang="en")

        # Step 3: Define output file name
        file_name = "user_audio.mp3"

        # Step 4: Save audio file
        tts.save(file_name)

        # Success message
        print(f"✅ Audio created successfully: {file_name}")

    except KeyboardInterrupt:
        print("\n❌ Program interrupted by user.")

    except Exception as e:
        print("❌ Something went wrong.")
        print("Error details:", e)


if __name__ == "__main__":
    text_to_speech()
