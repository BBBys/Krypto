#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Krypto/IndexKey © 2026 by Dr. Burkhard Borys
# is licensed under CC BY-NC-ND 4.0.
#
# KrIndexCode.py
#
# Wichtig:
# export PYTHONPATH="../Kryptolib"
#

import argparse, logging, string, os
from KrVorbereitung import *

# from KrPrint import print5
from ixkey import *

TITEL = "KrIndexCode"
VERSION = "V1.1"
DESCRIPTION = """Verschlüsselung eines Textes mit einem Index-Key"""


def main(eindatei, schlüsseldatei, ausdatei, Dbg):
    with open(schlüsseldatei, "rt") as fEin:
        ixkey = fEin.read()
    print(f"{len(ixkey)}\tZeichen im Schlüssel")

    zeilenEin = ZeilenAus = ZeichenEin = 0
    with open(eindatei, "rt") as fEin, open(ausdatei, "wt") as fAus:
        zeile = fEin.readline()
        while len(zeile) > 0:
            # noch nicht zuende
            lZeile = len(zeile)
            ZeichenEin += lZeile
            zeilenEin += 1

            if lZeile < 2:
                # Leerzeile
                zeile = fEin.readline()
                continue
            # len(txt) für leere Zeilen ist =1,
            # da das Zeilenende \n mitgelesen wird.
            zeile = KrVorbereitung(zeile)
            cipher = IxKeyEnc(zeile, ixkey)
            fAus.write(str(cipher) + "\n")
            ZeilenAus += 1

            if zeilenEin % 80 == 0:
                print(f"\n{zeilenEin}\tZeilen")
                print(f"{ZeichenEin}\tZeichen gelesen")
                print(f"{ZeilenAus}\tZeilen geschrieben")
            zeile = fEin.readline()

    print(f"\n{zeilenEin}\tZeilen")
    print(f"{ZeichenEin}\tZeichen gelesen")
    print(f"{ZeilenAus}\tZeilen geschrieben")


if __name__ == "__main__":
    import argparse, sys, logging

    # ------------------------------------------------------------
    # Parser-Objekt erstellen
    parser = argparse.ArgumentParser(description=DESCRIPTION, epilog=VERSION)
    # ------------------------------------------------------------
    # Übergabe mit Position
    parser.add_argument("Text", help="Eingabedatei, wird verschlüsselt")
    parser.add_argument("Key", help="Schlüsseldatei, die den Schlüssel enthält")
    parser.add_argument(
        "Aus", help="Ausgabedatei, in die das Ergebnis geschrieben wird"
    )
    parser.add_argument(
        "-v", "--debug", dest="pDbg", help="Debug-Ausgabe", action="store_true"
    )
    # ------------------------------------------------------------
    arguments = parser.parse_args()
    # Debug-Modus setzen
    Dbg = arguments.pDbg
    if Dbg:
        logging.basicConfig(level=logging.DEBUG)
    else:
        logging.basicConfig(level=logging.ERROR)
    eingabe = arguments.Text
    schlüssel = arguments.Key
    ausgabe = arguments.Aus
    if not os.path.exists(eingabe):
        logging.exception(f"Eingabedatei, Pfad {eingabe} existiert nicht.")
        raise Exception(f"{eingabe} existiert nicht.")
    if not os.path.exists(schlüssel):
        logging.exception(f"Schlüssel, Pfad {schlüssel} existiert nicht.")
        raise Exception(f"Pfad {schlüssel} existiert nicht.")

    # ------------------------------------------------------------
    # Programm aufrufen
    main(eingabe, schlüssel, ausgabe, Dbg)
    sys.exit(99)
