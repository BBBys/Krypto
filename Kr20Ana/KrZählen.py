def count_ngrams(text, n):
    """Zählt n-Gramme im Text.
    Ergebnis: Pandas Datafile mit n-Grammen und deren Häufigkeit."""
    return Counter(text[i : i + n] for i in range(len(text) - n + 1))


def save_counter_to_csv(counter, filename):
    """Speichert Counter als CSV-Datei."""
    df = pd.DataFrame(counter.items(), columns=["ngram", "count"])
    df = df.sort_values("count", ascending=False)
    df.to_csv(filename, index=False)
