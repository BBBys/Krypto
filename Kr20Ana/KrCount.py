#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Krypto/Zählen © 2026 by Dr. Burkhard Borys
# is licensed under CC BY-NC-ND 4.0.
#
# KrCount.py
#
# Wichtig:
# export PYTHONPATH="../Kryptolib"
#

import logging, os, time
import pandas as pd
from collections import Counter
from string import Template
from KrKoiIx import koiIx

TITEL = "KrCount"
VERSION = "V1.0"
DESCRIPTION = """Ermittelt die Häufigkeit von Zeichen, Bi- und 
Trigrammen in einem Text"""


def main(ein, aus, Dbg):
    mldEnde = Template(
        """
=======================================================
>>> Ergebnisse
    Auswertung eines Textes der Länge $laenge Zeichen

1.
$ng1 Zeichen ($nu1 unterschiedliche) in $z1 Sekunden
Koinzidenz-Index: $k1
2.
$ng2 Bi-Gramme ($nu2 unterschiedliche) in $z2 Sekunden
Koinzidenz-Index: $k2
3.
$ng3 Tri-Gramme ($nu3 unterschiedliche) in $z3 Sekunden
Koinzidenz-Index: $k3   
4.
$ng4 Quad-Gramme ($nu4 unterschiedliche) in $z4 Sekunden
Koinzidenz-Index: $k4
5.
$ng5 Penta-Gramme ($nu5 unterschiedliche) in $z5 Sekunden
Koinzidenz-Index: $k5
6.
$ng6 Hexa-Gramme ($nu6 unterschiedliche) in $z6 Sekunden
Koinzidenz-Index: $k6
7.
$ng7 Hepta-Gramme ($nu7 unterschiedliche) in $z7 Sekunden
Koinzidenz-Index: $k7

>>> Bewertung Koinzidenz-Index:
    Richtwerte: deutsch: 7,8%, englisch: 6,5%, zufällig: 3,8%
"""
    )

    text = read_clean_text(ein)
    länge = len(text)

    # 1
    startzeit = time.time()
    mono = count_ngrams(text, 1)
    stoppzeit = time.time()
    k1 = koiIx(mono, länge)
    z1 = stoppzeit - startzeit
    nu1 = len(mono)
    ng1 = sum(mono.values())
    save_counter_to_csv(mono, "monogramme.csv")

    # 2
    startzeit = time.time()
    bi = count_ngrams(text, 2)
    k2 = koiIx(bi, länge - 1)
    stoppzeit = time.time()
    z2 = stoppzeit - startzeit
    nu2 = len(bi)
    ng2 = sum(bi.values())
    save_counter_to_csv(bi, "bigramme.csv")

    # 3
    startzeit = time.time()
    tri = count_ngrams(text, 3)
    k3 = koiIx(tri, länge - 2)
    stoppzeit = time.time()
    z3 = stoppzeit - startzeit
    nu3 = len(tri)
    ng3 = sum(tri.values())
    save_counter_to_csv(tri, "trigramme.csv")

    startzeit = time.time()
    quad = count_ngrams(text, 4)
    k4 = koiIx(quad, länge - 3)
    stoppzeit = time.time()
    z4 = stoppzeit - startzeit
    nu4 = len(quad)
    ng4 = sum(quad.values())
    save_counter_to_csv(quad, "quadgramme.csv")

    startzeit = time.time()
    penta = count_ngrams(text, 5)
    k5 = koiIx(penta, länge - 4)
    stoppzeit = time.time()
    z5 = stoppzeit - startzeit
    nu5 = len(penta)
    ng5 = sum(penta.values())
    save_counter_to_csv(penta, "pentagramme.csv")
    startzeit = time.time()

    hexa = count_ngrams(text, 6)
    k6 = koiIx(hexa, länge - 5)
    stoppzeit = time.time()
    z6 = stoppzeit - startzeit
    nu6 = len(hexa)
    ng6 = sum(hexa.values())
    save_counter_to_csv(hexa, "hexagramme.csv")
    startzeit = time.time()

    hepta = count_ngrams(text, 7)
    stoppzeit = time.time()
    k7 = koiIx(hepta, länge - 6)
    z7 = stoppzeit - startzeit
    nu7 = len(hepta)
    ng7 = sum(hepta.values())
    save_counter_to_csv(hepta, "heptagramme.csv")

    print(
        mldEnde.substitute(
            laenge=f"{länge}",
            z1=f"{z1:.3f}",
            z2=f"{z2:.3f}",
            z3=f"{z3:.3f}",
            z4=f"{z4:.3f}",
            z5=f"{z5:.3f}",
            z6=f"{z6:.3f}",
            z7=f"{z7:.3f}",
            nu1=nu1,
            nu2=nu2,
            nu3=nu3,
            nu4=nu4,
            nu5=nu5,
            nu6=nu6,
            nu7=nu7,
            ng1=ng1,
            ng2=ng2,
            ng3=ng3,
            ng4=ng4,
            ng5=ng5,
            ng6=ng6,
            ng7=ng7,
            k1=f"{k1:.4f}",
            k2=f"{k2:.4f}",
            k3=f"{k3:.4f}",
            k4=f"{k4:.4f}",
            k5=f"{k5:.4f}",
            k6=f"{k6:.4f}",
            k7=f"{k7:.4f}",
        )
    )


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
    main(ein, arguments.aus, Dbg)
