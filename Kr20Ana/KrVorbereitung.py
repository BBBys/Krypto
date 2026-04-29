#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Krypto/Vorbereitung © 2026 by Dr. Burkhard Borys
# is licensed under CC BY-NC-ND 4.0.
#
# KrVorbereitung.py
#
# Wichtig:
# export PYTHONPATH="../Kryptolib"
#

import logging, os
from KrZeichensatz import KrZeichen

TITEL = "KrVorbereitung"
VERSION = "V1.0"
DESCRIPTION = """kopiert eine Datei mit Text, beschränkt dabei den Zeichenvorrat 
auf die gewünschten Zeichen"""


def main(ein, aus, länge, Dbg):
    # einlesen, vorbereiten, Kontrolle:
    with open(ein, "r") as f:
        txt = f.read()
    l1 = len(txt)
    print(f"{l1:<8} Zeichen von {ein} gelesen")
    txt = KrZeichen(txt)
    l2 = len(txt)
    print(f"{l2:<8} ({l2/l1*100:.1f}%) Großbuchstaben verbleiben")
    l3 = l2 // 3
    print(txt[l3 : l3 + 80])
    # ausgeben:
    with open(aus, "wt") as f:
        i = 0
        z = 0
        while i < len(txt):
            f.write(txt[i : i + länge]+"\n")
            i += länge
            z += 1
    print(f"{z} Zeilen auf {aus} geschrieben")


if __name__ == "__main__":
    import argparse, sys, logging

    # ------------------------------------------------------------
    # Parser-Objekt erstellen
    parser = argparse.ArgumentParser(description=DESCRIPTION, epilog=VERSION)
    # ------------------------------------------------------------
    # Übergabe mit Position
    parser.add_argument("ein", type=str, help="Eingabedatei")
    parser.add_argument("aus", type=str, help="Ausgabedatei")
    parser.add_argument(
        "-l",
        "--länge",
        dest="länge",
        type=int,
        default=80,
        help="Zeilenlänge, Unterteilung der Ausgabedatei",
    )
    parser.add_argument(
        "-v", "--debug", dest="pDbg", help="Debug-Ausgabe", action="store_true"
    )
    # ------------------------------------------------------------
    # Debug-Modus setzen
    arguments = parser.parse_args()
    Dbg = arguments.pDbg
    if Dbg:
        logging.basicConfig(level=logging.DEBUG)
    else:
        logging.basicConfig(level=logging.ERROR)
    ein = arguments.ein
    if not os.path.exists(ein):
        logging.exception(f"Pfad {ein} existiert nicht.")
        raise Exception(f"Pfad {ein} existiert nicht.")
    # ------------------------------------------------------------
    # Programm aufrufen
    main(ein, arguments.aus, arguments.länge, Dbg)
