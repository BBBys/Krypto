def read_clean_text(path):
    """Liest Textdatei und entfernt Zeilenumbrüche."""
    with open(path, "r", encoding="utf-8") as f:
        text = f.read()
    return text.replace("\n", "").strip()
