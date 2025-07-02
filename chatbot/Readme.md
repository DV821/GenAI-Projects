
# 🤖 GenAI Chatbot Projects

This repository contains two chatbot applications built with LangChain:

- `openai_app.py`: A cloud-based chatbot using OpenAI's GPT models
- `locallama_app.py`: A fully local chatbot using the Gemma 3B model via Ollama

Both bots demonstrate how to create natural language assistants using different large language model (LLM) backends — one hosted (OpenAI), the other local (Gemma via Ollama).

---

## 📌 Project Overview

| File               | Model Used       | Hosted/Local | Key Tech              |
|--------------------|------------------|--------------|-----------------------|
| `openai_app.py`    | OpenAI GPT-4     | Cloud        | OpenAI API, LangChain |
| `locallama_app.py` | Gemma 3          | Local        | Ollama, LangChain     |

---

## 🧰 Requirements

- Python 3.11
- `pip` or `conda`
- (Optional) [Ollama](https://ollama.com) for running local models

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## 🔐 Environment Setup

Create a `.env` file in the root directory for OpenAI usage:

```ini
# .env
OPENAI_API_KEY = openai_key_here
LANGCHAIN_API_KEY = langchain_api_key
```

---

## 🚀 Running the Chatbots

### 1. 💬 OpenAI GPT Chatbot (`openai_app.py`)

This version uses OpenAI's hosted models via API.

```bash
streamlit run openai_app.py
```

✅ Features:

- Maintains conversation context
- Uses LangChain for prompt management
- Requires an OpenAI API key

---

### 2. 🏠 Local LLM Chatbot (`locallama_app.py`)

This version uses the Gemma 3B model running locally via Ollama.

#### Step 1: Install Ollama

Download and install Ollama:  
👉 [https://ollama.com](https://ollama.com)

#### Step 2: Pull the Gemma model

```bash
ollama run gemma3:1b
```

#### Step 3: Run the chatbot

Make sure the Ollama service is running:

```bash
streamlit run locallama_app.py
```

✅ Features:

- Runs entirely offline
- Private and local
- Same conversational flow as OpenAI version

---

## 📁 Project Structure

```
chatbot/
├── openai_app.py         # Cloud-based chatbot using OpenAI GPT
├── locallama_app.py      # Local chatbot using Gemma 3B via Ollama
├── requirements.txt
├── .env
└── README.md
```

---

## 🧩 Extension Ideas

- Integrate PDF/CSV/document ingestion for RAG (Retrieval-Augmented Generation)
- Add a web frontend using Streamlit or FastAPI
- Support additional models via Ollama (LLaMA 3, Mistral, Phi, etc.)
- Log conversations or user queries to a database or file
- Add multi-user sessions and authentication

---

## 🙌 Acknowledgments

- OpenAI for GPT APIs
- Ollama for local model serving
- LangChain for framework support
