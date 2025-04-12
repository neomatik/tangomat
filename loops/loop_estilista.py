from agents.estilista import estilista
from utils.guardar_seccion import guardar_seccion

# Simulación de varias secciones por capítulo
# En el flujo real, esto se integraría con planificación y flujo automático

capitulo = 2
secciones = 3  # Número de secciones por capítulo

for i in range(1, secciones + 1):
    print(f"✍️ Generando sección {i} del capítulo {capitulo}...")
    response = estilista.run()
    guardar_seccion(response, capitulo=capitulo, seccion=i)
