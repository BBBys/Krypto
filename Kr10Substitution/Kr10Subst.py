#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Krypto/Substitution © 2026 by Dr. Burkhard Borys
# is licensed under CC BY-NC-ND 4.0.
#
# KrSubst.py
import argparse, logging
from monosubst import *

TITEL = "Kr10Subst"
VERSION = "V0.0"
DESCRIPTION = """Behandlung von Substitutions-Codes"""


def main(Dbg, Mono):
    if Mono:
        from monosubst import substenc, substdec
        # ------------------------------------------------------------
        # Test
        txt = "Hallo, wie geht es dir?"
        key = "QWERTZUIOPASDFGHJKLYXCVBNM"
        cipher = substenc(txt, key)
        logging.debug(f"Verschlüsselt: {cipher}")
        key = "QWERTZIUOAPSDFGHJKLYXVCBNM"
        klar = substdec(cipher, key)
        logging.debug(f"Entschlüsselt: {klar}")


if __name__ == "__main__":
    import argparse, sys, logging

    # ------------------------------------------------------------
    # Parser-Objekt erstellen
    parser = argparse.ArgumentParser(description=DESCRIPTION)
    # ------------------------------------------------------------
    # Übergabe mit Position
    # parser.add_argument('pNumber', type=int, help='Eine Zahl')
    parser.add_argument("-v", "--debug", dest="pDbg", 
                        help="Debug-Ausgabe", action="store_true")
    parser.add_argument("-m", "--mono", dest="pMono",
                        help="Monoalphatbetische Substitution", 
                        action="store_true")
    # ------------------------------------------------------------
    arguments = parser.parse_args()
    # Debug-Modus setzen
    Dbg = arguments.pDbg
    if Dbg:
        logging.basicConfig(level=logging.DEBUG)
    else:
        logging.basicConfig(level=logging.ERROR)
    
    # ------------------------------------------------------------
    # Programm aufrufen
    main(Dbg, arguments.pMono)
