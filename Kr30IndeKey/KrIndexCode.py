#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Krypto/IndexKey © 2026 by Dr. Burkhard Borys
# is licensed under CC BY-NC-ND 4.0.
#
# KrIndexKey.py
#
# Wichtig:
# export PYTHONPATH="../Kryptolib"
#

import argparse, logging, string, os
from KrVorbereitung import *
from KrPrint import print5
from ixkey import *

TITEL = "KrIndexKey"
VERSION = "V1.1"
DESCRIPTION = """Aufbau eines Index-Keys aus einem Schlüsseltext"""


def main(sdatei, kdatei, länge, Dbg):
    with open(sdatei, "r") as f:
        txt = f.read()
    schlüssel = "FC Bayern in der Champions League: Ein Albtraum, aus dem es kein Erwachen gibt. Erst patzt Manuel Neuer, dann der Schiedsrichter: Das unglückliche Aus im Halbfinale stürzt den FC Bayern in tiefe Schockstarre. Ein höchst emotionaler Thomas Tuchel schwankt zwischen Trauer, Wut und Verzweiflung. Lachs aus Aquakulturen: »Die Menschen wollen keinen Lachs essen, für den die Umwelt zerstört wird«. In Norwegen wird das Angeln von Wildlachs eingeschränkt, um die Tiere zu schützen. In Kanada sollen Aquakulturen verschwinden, weil sie Ökosysteme zerstören. Wissenschaftler Eirik Biering sagt, was sich bei der Fischzucht ändern muss."
    schlüssel = KrVorbereitung(schlüssel)
    schlüssel = schlüssel[:länge]
    txt = KrVorbereitung(txt)
    if Dbg:
        logging.debug("Schlüssel:")
        print5(schlüssel)
        logging.debug("Text:")
        print5(txt)

    ixkey = []
    for i in range(len(schlüssel)):
        c = schlüssel[i]
        ixkey.append(c)

    # was fehlt?
    fehlt = []
    for c in string.ascii_uppercase:
        if c not in ixkey:
            fehlt.append(c)
    lf = len(fehlt)
    if lf > 0:
        logging.debug(f"Fehlende Zeichen: {fehlt}")
        ixkey += fehlt
    else:
        logging.debug("Alle Zeichen vorhanden")
    logging.debug(f"Index-Key: {ixkey}")
    with open(kdatei, "wt") as f:
        for c in ixkey:
            f.write(c)
            f.write("\n")


    cipher = IxKeyEnc(txt, ixkey)
    logging.debug(f"Verschlüsselt: {cipher}")

    print5(cipher)


if __name__ == "__main__":
    import argparse, sys, logging

    # ------------------------------------------------------------
    # Parser-Objekt erstellen
    parser = argparse.ArgumentParser(description=DESCRIPTION, epilog=VERSION)
    # ------------------------------------------------------------
    # Übergabe mit Position
    parser.add_argument(
        "SText",
        help="Datei mit Text, aus dem der Schlüssel gebildet wird",
        default=sys.stdin,
    )
    parser.add_argument(
        "Key",
        default=sys.stdout,
        help="Datei, die den Schlüssel erhält",
    )
    parser.add_argument(
        "-v", "--debug", dest="pDbg", help="Debug-Ausgabe", action="store_true"
    )
    parser.add_argument(
        "-l",
        "--länge",
        dest="Länge",
        help="Länge des Index-Keys [9999]",
        type=int,
        default=9999,
    )
    # ------------------------------------------------------------
    arguments = parser.parse_args()
    # Debug-Modus setzen
    Dbg = arguments.pDbg
    if Dbg:
        logging.basicConfig(level=logging.DEBUG)
    else:
        logging.basicConfig(level=logging.ERROR)
    sfile = arguments.SText
    kfile = arguments.Key
    if not os.path.exists(sfile):
        logging.exception(f"Pfad {sfile} existiert nicht.")
        raise Exception(f"Pfad {sfile} existiert nicht.")

    # ------------------------------------------------------------
    # Programm aufrufen
    main(sfile, kfile, arguments.Länge, Dbg)
