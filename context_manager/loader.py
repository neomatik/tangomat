import os

def load_chapter_context(chapter_number):
    path = f"story/chapters/cap_{chapter_number:02d}/"
    full_context = ""

    if not os.path.exists(path):
        return ""

    for fname in sorted(os.listdir(path)):
        if fname.endswith(".md"):
            with open(os.path.join(path, fname), "r", encoding="utf-8") as f:
                full_context += f"\n\n---\n\n# {fname}\n\n" + f.read()

    return full_context
