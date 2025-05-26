# 🧠 LangGraph Chatbot with Ollama

A simple chatbot using [LangGraph](https://github.com/langchain-ai/langgraph) 
and [Ollama](https://ollama.com) with a state machine and a custom UTC time tool.

---

## 🚀 Features

- Stateless LLM-based conversation
- Dynamic UTC time tool (`get_current_time`)
- Built on `LangGraph`, `LangChain`, and `Ollama`

---

## 🧱 Requirements

- Python 3.10+
- Ollama running locally (tested with `llama3
(ollama pull llama3 -> ollama run llama3)
- Virtual environment recommended

---

## 🛠 Setup

```bash
# Clone the repository
git clone https://github.com/Nident/langgraph-chatbot.git
cd langgraph-chatbot

# Create virtual environment
python3.10 -m venv .venv
source .venv/bin/activate  # on Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
