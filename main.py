import asyncio
import edge_tts

async def improve_audio():
    TEXT = "Welcome to your improved text-to-audio project with neural voices!"
    VOICE = "en-US-GuyNeural" # High-quality Microsoft voice
    OUTPUT_FILE = "improved_audio.mp3"
    
    communicate = edge_tts.Communicate(TEXT, VOICE)
    await communicate.save(OUTPUT_FILE)
    print(f"Saved to {OUTPUT_FILE}")

asyncio.run(improve_audio())
