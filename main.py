import asyncio
import edge_tts

async def improve_audio():
    # 1. Added more natural text
    TEXT = "Welcome! This is an optimized version of your text-to-audio project."
    
    # 2. You can experiment with different voices 
    # Use 'python -m edge_tts --list-voices' in your terminal to see all options
    VOICE = "en-US-GuyNeural" 
    
    # 3. Added customization parameters
    # Rate: +0% is default. Use +20% to speed up or -10% to slow down.
    # Pitch: +0Hz is default. Use +50Hz for higher or -20Hz for lower tone.
    RATE = "+5%"
    PITCH = "+0Hz"
    VOLUME = "+0%"
    
    OUTPUT_FILE = "improved_audio.mp3"
    
    # 4. Initialize with new parameters
    communicate = edge_tts.Communicate(
        text=TEXT, 
        voice=VOICE, 
        rate=RATE, 
        pitch=PITCH, 
        volume=VOLUME
    )
    
    print(f"Generating audio for: '{TEXT}'...")
    
    # 5. Saving the file
    await communicate.save(OUTPUT_FILE)
    print(f"Successfully saved to {OUTPUT_FILE}")

if __name__ == "__main__":
    asyncio.run(improve_audio())
