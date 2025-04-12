import os

def consolidar_capitulo(capitulo=1):
    """
    Une todas las secciones de un capítulo en un único archivo markdown.

    Args:
        capitulo (int): Número del capítulo a consolidar.
    """
    cap_dir = f"story/chapters/cap_{capitulo:02d}"
    secciones = sorted(f for f in os.listdir(cap_dir) if f.startswith("sec_") and f.endswith(".md"))
    consolidado = ""

    for nombre in secciones:
        with open(os.path.join(cap_dir, nombre), "r", encoding="utf-8") as f:
            texto = f.read().strip()
            consolidado += f"# {nombre}\n\n{texto}\n\n---\n\n"

    salida = os.path.join(cap_dir, "capitulo_completo.md")
    with open(salida, "w", encoding="utf-8") as f:
        f.write(consolidado.strip())

    print(f"📘 Capítulo {capitulo} consolidado en: {salida}")
