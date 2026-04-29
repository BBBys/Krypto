#!/usr/bin/env python
# -*- coding: utf-8 -*-
import string

# Monoalphabetische Substitution
# Verschlüsselung, Entschlüsselung


def substenc(txt, key):
    alphabet = string.ascii_uppercase
    map = {alphabet[i]: key[i] for i in range(26)}

    cipher = []
    for ch in txt.upper():
        if ch in map:
            cipher.append(map[ch])
        else:
            cipher.append(ch)  # Sonderzeichen bleiben erhalten
    return "".join(cipher)


def substdec(cipher, schluessel):
    alphabet = string.ascii_uppercase
    rmap = {schluessel[i]: alphabet[i] for i in range(26)}

    klar = []
    for ch in cipher.upper():
        if ch in rmap:
            klar.append(rmap[ch])
        else:
            klar.append(ch)
    return "".join(klar)
