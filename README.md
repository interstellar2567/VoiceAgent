# 🎙️ AI Voice Agent Web App

This is a simple web-based AI Voice Agent that supports:

- ✅ Text-to-Speech (TTS) conversion using FastAPI backend
- ✅ Echo Bot that records and plays back your own voice using the MediaRecorder API

> Built as part of the [30 Days of AI Voice Agents Challenge](https://www.linkedin.com/feed/hashtag/30daysofaivoiceagents/) by [MURF AI](https://murf.ai/)

---

## 🧩 Features

### 1. Text to Speech (TTS)
- Input any text
- Sends it to a FastAPI `/generate` endpoint
- Returns an audio URL and plays the generated voice

### 2. Echo Bot
- Uses your microphone to record a short voice clip
- Instantly plays your voice back using `<audio>` player
- Built using the browser's `MediaRecorder` API

.....and many more features to be included
---

## 🛠️ Tech Stack

| Frontend      | Backend     |
|---------------|-------------|
| HTML, CSS, JS | FastAPI,Flask     |

---

## 📦 Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/ai-voice-agent.git
cd ai-voice-agent
