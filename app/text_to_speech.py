import pyttsx3

engine = pyttsx3.init()

# Speed
engine.setProperty("rate", 170)

# Volume (0.0 - 1.0)
engine.setProperty("volume", 1.0)

# Get available voices
voices = engine.getProperty("voices")

print("\nAvailable Voices:\n")

for i, voice in enumerate(voices):
    print(f"{i}: {voice.name}")
    print(f"   ID: {voice.id}")
    print("-" * 50)

# Select voice
# Change 0 to 1 if you want another voice
engine.setProperty("voice", voices[1].id)


def speak(text: str):
    engine.say(text)
    engine.runAndWait()


if __name__ == "__main__":
    speak("Hello Golam. Welcome to your Voice AI Assistant.")