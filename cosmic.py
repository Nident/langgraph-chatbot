from datetime import datetime, timezone
from typing import Dict
from langgraph.graph import StateGraph, END
from langchain_ollama import ChatOllama
from langchain_core.tools import tool

# Инструмент: получить текущее UTC время
@tool
def get_current_time() -> Dict[str, str]:
    """Return the current UTC time in ISO‑8601 format."""
    now = datetime.now(timezone.utc)
    return {"utc": now.isoformat()}

# Подключение Ollama
llm = ChatOllama(model="llama3", base_url="http://localhost:11434")

def chat_node(state: str) -> Dict[str, str]:
    if "time" in state.lower():
        time_value = get_current_time.invoke("")["utc"]
        return {"response": f"The current UTC time is {time_value}"}
    else:
        result = llm.invoke(state)
        return {"response": result.content}

# Сборка графа
builder = StateGraph(state_schema=str)
builder.add_node("chat", chat_node)

# Stateless: один ответ → завершение
builder.add_conditional_edges(
    "chat",
    {
        END: lambda _: True  # Всегда переход к завершению
    }
)

builder.set_entry_point("chat")
app = builder.compile()

# Цикл чата
def run_chatbot() -> None:
    print("🤖 Chatbot started. Type 'exit' to quit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            break
        result = app.invoke(user_input)
        print("Bot:", result["response"])

if __name__ == "__main__":
    run_chatbot()