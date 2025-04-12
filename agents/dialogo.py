from crewai import Agent
from pathlib import Path

def load_prompt():
    with open(Path("prompts/dialogo.md"), "r", encoding="utf-8") as f:
        return f.read()

dialogo = Agent(
    role="Editor de Diálogo",
    goal="Mejorar la naturalidad, tensión y autenticidad de los diálogos.",
    backstory="Dramaturgo y lingüista especializado en conversaciones con voz propia.",
    verbose=True,
    allow_delegation=False,
    llm_config={
        "config": {
            "model": "gpt-4",
            "temperature": 0.7
        }
    },
    prompt=load_prompt()
)
