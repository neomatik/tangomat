from crewai import Agent
from pathlib import Path

def load_prompt():
    with open(Path("prompts/estilista.md"), "r", encoding="utf-8") as f:
        return f.read()

estilista = Agent(
    role="Estilista Literario",
    goal="Escribir secciones narrativas desde el punto de vista de Elías Navarro.",
    backstory="Experto en estilo literario neo-noir, trabaja con precisión clínica.",
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
