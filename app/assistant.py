from app.speech_to_text import record_audio, speech_to_text
from app.text_to_speech import speak
from app.llm import chat


def run():
    while True:
        print("\n🎤 Speak... (Say 'exit' to quit)")

        record_audio()

        user_text = speech_to_text()

        print(f"\nYou: {user_text}")

        if user_text.lower() == "exit":
            speak("Goodbye!")
            break

        response = chat(user_text)

        print(f"\nAI: {response}")

        speak(response)