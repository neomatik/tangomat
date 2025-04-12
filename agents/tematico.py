from crewai import Agent
from pathlib import Path

def load_prompt():
    with open(Path("prompts/tematico.md"), "r", encoding="utf-8") as f:
        return f.read()

tematico = Agent(
    role="Analista Temático",
    goal="Detectar ejes simbólicos, dilemas filosóficos y fracturas estructurales.",
    backstory="Teórico literario obsesionado con el simbolismo profundo y la narrativa cerebral.",
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
