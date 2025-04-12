from crewai import Agent
from pathlib import Path

def load_prompt():
    with open(Path("prompts/cientifico.md"), "r", encoding="utf-8") as f:
        return f.read()

cientifico = Agent(
    role="Consultor Científico",
    goal="Verificar la plausibilidad y rigor del contenido técnico.",
    backstory="Investigador multidisciplinar entre ciencia dura y filosofía racional.",
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
