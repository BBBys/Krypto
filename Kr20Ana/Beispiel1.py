import string


def substitution_encrypt(text, schluessel):
    alphabet = string.ascii_uppercase
    mapping = {alphabet[i]: schluessel[i] for i in range(26)}

    ergebnis = []
    for ch in text.upper():
        if ch in mapping:
            ergebnis.append(mapping[ch])
        else:
            ergebnis.append(ch)  # Sonderzeichen bleiben erhalten
    return "".join(ergebnis)


text = "Hallo Welt"
schluessel = "QWERTZUIOPASDFGHJKLYXCVBNM"

cipher = substitution_encrypt(text, schluessel)
print(cipher)


def substitution_decrypt(cipher, schluessel):
    alphabet = string.ascii_uppercase
    reverse_map = {schluessel[i]: alphabet[i] for i in range(26)}

    ergebnis = []
    for ch in cipher.upper():
        if ch in reverse_map:
            ergebnis.append(reverse_map[ch])
        else:
            ergebnis.append(ch)
    return "".join(ergebnis)
