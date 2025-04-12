from crewai import Agent
from pathlib import Path

def load_prompt():
    with open(Path("prompts/personajes.md"), "r", encoding="utf-8") as f:
        return f.read()

personajes = Agent(
    role="Agente de Personajes",
    goal="Evaluar la consistencia emocional y evolución de los personajes.",
    backstory="Psicólogo literario, experto en arcos de personaje y motivación.",
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
