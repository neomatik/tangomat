from crewai import Agent
from pathlib import Path

def load_prompt():
    with open(Path("prompts/coherencia.md"), "r", encoding="utf-8") as f:
        return f.read()

coherencia = Agent(
    role="Supervisor de Coherencia",
    goal="Garantizar la continuidad lógica y narrativa del capítulo.",
    backstory="Editor meticuloso con ojo clínico para inconsistencias y errores sutiles.",
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
