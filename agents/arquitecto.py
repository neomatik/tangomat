from crewai import Agent
from pathlib import Path

def load_prompt():
    with open(Path("prompts/arquitecto.md"), "r", encoding="utf-8") as f:
        return f.read()

arquitecto = Agent(
    role="Arquitecto Narrativo",
    goal="Diseñar la estructura narrativa de cada capítulo.",
    backstory="Experto en arquitectura narrativa. Define secciones, tono y ritmo.",
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
