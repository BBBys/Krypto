import string
from collections import Counter

"""
---------------------------------------------------------
1) Substitutions-Verschlüsselung
---------------------------------------------------------
"""


def substitution_encrypt(text, key):
    alphabet = string.ascii_uppercase
    mapping = {alphabet[i]: key[i] for i in range(26)}

    result = []
    for ch in text.upper():
        if ch in mapping:
            result.append(mapping[ch])
        else:
            result.append(ch)
    return "".join(result)


def substitution_decrypt(cipher, key):
    alphabet = string.ascii_uppercase
    reverse_map = {key[i]: alphabet[i] for i in range(26)}

    result = []
    for ch in cipher.upper():
        if ch in reverse_map:
            result.append(reverse_map[ch])
        else:
            result.append(ch)
    return "".join(result)


"""
---------------------------------------------------------
2) Frequenzanalyse-Angriff (monogram-based)
---------------------------------------------------------
"""

ENGLISH_FREQ_ORDER = "ETAOINSHRDLCUMWFGYPBVKJXQZ"


def frequency_attack(cipher):
    # Nur Buchstaben zählen
    letters_only = [c for c in cipher.upper() if c in string.ascii_uppercase]
    freq = Counter(letters_only)

    # Sortiere Cipher-Buchstaben nach Häufigkeit
    cipher_sorted = [item[0] for item in freq.most_common()]

    # Baue Mapping: häufigster Cipher-Buchstabe -> 'E', zweit-häufigster -> 'T', ...
    mapping = {}
    for i, c in enumerate(cipher_sorted):
        if i < len(ENGLISH_FREQ_ORDER):
            mapping[c] = ENGLISH_FREQ_ORDER[i]

    # Wende Mapping an
    result = []
    for ch in cipher.upper():
        if ch in mapping:
            result.append(mapping[ch])
        else:
            result.append(ch)
    return "".join(result), mapping


"""
---------------------------------------------------------
3) Demo
---------------------------------------------------------
"""


if __name__ == "main":
    text = "DIES IST EIN GEHEIMER TEXT, DER MIT SUBSTITUTION VERSCHLUESSELT WURDE."
    key = "QWERTZUIOPASDFGHJKLYXCVBNM"  # Beispielschlüssel

    cipher = substitution_encrypt(text, key)
    print("Ciphertext:")
    print(cipher)
    print()

    guess, mapping = frequency_attack(cipher)
    print("Frequenzanalyse (Best Guess):")
    print(guess)
    print()

    print("Verwendetes Mapping (Cipher -> Vermuteter Klartext):")
    for c, p in mapping.items():
        print(f"{c} -> {p}")
