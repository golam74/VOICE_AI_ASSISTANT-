import sounddevice as sd
from scipy.io.wavfile import write
from faster_whisper import WhisperModel

model = WhisperModel(
    "small",
    device="cpu",
    compute_type="int8"
)

def record_audio(filename="record.wav", duration=8, sample_rate=16000):
    print("🎤 Speak...")

    recording = sd.rec(
        int(duration * sample_rate),
        samplerate=sample_rate,
        channels=1,
        dtype="int16"
    )

    sd.wait()

    write(filename, sample_rate, recording)

    print("✅ Recording Finished")

def speech_to_text(filename="record.wav"):
    segments, _ = model.transcribe(filename)

    text = ""

    for segment in segments:
        text += segment.text

    return text.strip()