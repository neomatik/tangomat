import os

def guardar_seccion(texto, capitulo=1, seccion=1):
    """
    Guarda una sección narrativa en la estructura del sistema.

    Args:
        texto (str): Texto generado por el Estilista.
        capitulo (int): Número del capítulo (ej. 2).
        seccion (int): Número de la sección (ej. 1).
    """
    cap_dir = f"story/chapters/cap_{capitulo:02d}"
    os.makedirs(cap_dir, exist_ok=True)

    filename = os.path.join(cap_dir, f"sec_{seccion:02d}.md")
    with open(filename, "w", encoding="utf-8") as f:
        f.write(texto.strip())

    print(f"✅ Sección guardada: {filename}")
