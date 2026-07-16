# 🎙️ Voice AI Assistant

A production-ready **Local Voice AI Assistant** built with **Python** and **Ollama**.

This project demonstrates how to build an intelligent voice assistant that can listen to user speech, convert speech to text, generate AI responses using a local Large Language Model (LLM), and reply using text-to-speech—all while running locally.

---

# ✨ Features

* 🎤 Speech-to-Text (STT)
* 🤖 Local AI Chat with Ollama
* 🔊 Text-to-Speech (TTS)
* 💬 Real-time Voice Conversation
* ⚡ Interactive Command Line Interface (CLI)
* 🔒 Runs Completely Offline
* 🏗 Modular Python Architecture

---

# 🛠 Tech Stack

* Python 3.11+
* Ollama
* Gemma 2B / Qwen 3
* Faster-Whisper
* Pyttsx3
* SoundDevice
* SciPy
* NumPy
* python-dotenv

---

# 📂 Project Structure

```text
Voice_AI_Assistant/
│
├── app/
│   ├── __init__.py
│   ├── assistant.py
│   ├── config.py
│   ├── llm.py
│   ├── prompts.py
│   ├── speech_to_text.py
│   └── text_to_speech.py
│
├── main.py
├── test.py
├── requirements.txt
├── .env
└── README.md
```

---

# 🚀 Getting Started

## 1. Clone the Repository

```bash
git clone https://github.com/golam74/Voice_AI_Assistant.git

cd Voice_AI_Assistant
```

---

## 2. Create a Virtual Environment

```bash
python -m venv venv
```

### Windows

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Install Ollama

Download and install Ollama from:

https://ollama.com

Pull a model:

```bash
ollama pull gemma2:2b
```

or

```bash
ollama pull qwen3:8b
```

---

## 5. Configure Environment Variables

Create a `.env` file in the project root.

```env
OLLAMA_HOST=http://localhost:11434
OLLAMA_MODEL=gemma2:2b
```

---

## 6. Run the Application

```bash
python main.py
```

---

# 💡 Example Conversation

```text
🎤 You:
Hello

🤖 AI:
Hello! How can I help you today?

🎤 You:
What is Artificial Intelligence?

🤖 AI:
Artificial Intelligence (AI) is the simulation of human intelligence by machines...

🎤 You:
Exit

🤖 AI:
Goodbye!
```

---

# 🏗 Architecture

```text
          User
            │
            ▼
      🎤 Microphone
            │
            ▼
    Speech-to-Text
   (Faster Whisper)
            │
            ▼
         Ollama
      Local LLM
            │
            ▼
     AI Response
            │
            ▼
     Text-to-Speech
       (pyttsx3)
            │
            ▼
        🔊 Speaker
```

---

# 📌 Key Learnings

During this project I learned:

* Building Local Voice AI Applications
* Speech-to-Text Pipelines
* Text-to-Speech Integration
* Ollama API Integration
* Prompt Engineering
* Modular Python Architecture
* Real-Time AI Conversations
* Offline AI Development

---

# 🚀 Future Improvements

* Wake Word Detection ("Hey Assistant")
* Continuous Listening Mode
* Conversation Memory
* Tool Calling
* Web Search Integration
* Weather Information
* Email Automation
* Smart Home Controls
* GUI using Streamlit
* FastAPI Backend
* Voice Cloning
* Multi-language Support

---

# 🤝 Contributing

Contributions are welcome!

If you'd like to improve this project, feel free to fork the repository, open an issue, or submit a pull request.

---

# 📄 License

This project is licensed under the MIT License.

---

# 👨‍💻 Author

**Golam Israil**

Aspiring AI Engineer

Building AI Agents • Voice AI • RAG Systems • LLM Applications • AI Automation

GitHub: https://github.com/golam74
