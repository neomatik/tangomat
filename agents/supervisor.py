from crewai import Agent
from pathlib import Path

def load_prompt():
    with open(Path("prompts/supervisor.md"), "r", encoding="utf-8") as f:
        return f.read()

supervisor = Agent(
    role="Agente Supervisor",
    goal="Integrar las evaluaciones y emitir informe global del capítulo.",
    backstory="Coordinador editorial con visión panorámica de calidad narrativa.",
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
