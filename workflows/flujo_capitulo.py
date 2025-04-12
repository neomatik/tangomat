# workflows/flujo_capitulo.py

from agents.arquitecto import arquitecto
from agents.estilista import estilista
from agents.personajes import personajes
from agents.dialogo import dialogo
from agents.coherencia import coherencia
from agents.tematico import tematico
from agents.cientifico import cientifico
from agents.supervisor import supervisor

from crewai import Crew, Task

# --------------------------------------------------------
# 🔧 TAREAS
# --------------------------------------------------------

# 1. Planificación del capítulo (estructura, tono, secciones)
planificacion = Task(
    description="Planificar el capítulo actual dividiéndolo en secciones detalladas con propósito, tono y progresión emocional.",
    agent=arquitecto
)

# 2. Redacción inicial por secciones (~1500 palabras cada una)
# La división es funcional, no narrativa. El Estilista guarda cada sección individualmente.
escritura = Task(
    description="Redactar las secciones del capítulo siguiendo el esquema del Arquitecto y el estilo establecido.",
    agent=estilista
)

# 3. Revisión del capítulo completo una vez estén todas las secciones

# Coherencia primero para detectar fallos estructurales
revisar_coherencia = Task(
    description="Verificar continuidad lógica y coherencia narrativa del capítulo.",
    agent=coherencia
)

# Validación de ciencia o lógica interna
revisar_ciencia = Task(
    description="Validar plausibilidad técnica y exactitud de referencias científicas.",
    agent=cientifico
)

# Evaluaciones específicas
revisar_personajes = Task(
    description="Revisar consistencia y evolución de los personajes en el texto generado.",
    agent=personajes
)

revisar_dialogo = Task(
    description="Evaluar naturalidad, tensión y estilo de los diálogos.",
    agent=dialogo
)

revisar_tematica = Task(
    description="Detectar temas subyacentes y sugerir formas de reforzarlos.",
    agent=tematico
)

# 4. Integración de comentarios en informe global
generar_informe = Task(
    description="Integrar todos los comentarios anteriores en un informe final para reescritura del capítulo.",
    agent=supervisor
)

# --------------------------------------------------------
# 🧠 CREW: definición del equipo y tareas del capítulo
# --------------------------------------------------------

flujo_capitulo = Crew(
    agents=[
        arquitecto,
        estilista,
        coherencia,
        cientifico,
        personajes,
        dialogo,
        tematico,
        supervisor
    ],
    tasks=[
        planificacion,
        escritura,
        revisar_coherencia,
        revisar_ciencia,
        revisar_personajes,
        revisar_dialogo,
        revisar_tematica,
        generar_informe
    ],
    verbose=True
)

# --------------------------------------------------------
# 🚀 Ejecutar flujo completo del capítulo
# --------------------------------------------------------

if __name__ == "__main__":
    flujo_capitulo.kickoff()
