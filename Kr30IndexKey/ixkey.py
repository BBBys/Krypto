# Verschlüsselung von Text mit Index-Schlüssel
# import logging
import random


def IxKeyEnc(klarText, ixkey):
    codeText = []
    for i in range(len(klarText)):
        klarZeichen = klarText[i]
        codeZeichen = getrandomkey(klarZeichen, ixkey)
        codeText.append(codeZeichen)
    return codeText


def getrandomkey(klarZeichen, ixkey):
    l = len(ixkey)
    index = random.randint(0, l - 1)
    versuch = 0
    while ixkey[index] != klarZeichen:
        index = (index + 1) % l
        versuch = versuch + 1
        if versuch > l + 1:
            raise Exception(f"Zeichen {klarZeichen} nicht im Schlüssel gefunden")
    return index
