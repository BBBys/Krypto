#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Krypto/Analyse © 2026 by Dr. Burkhard Borys
# is licensed under CC BY-NC-ND 4.0.
#
# KrAna.py
import argparse, logging
from string import Template
from häufigkeiten import *

TITEL = "KrAna - Kryptoanalyse"
VERSION = "V1.0"
DESCRIPTION = """Statistische Analyse eines Textes"""
GTEXT1 = """Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."""
GTEXT2 = "FC Bayern in der Champions League: Ein Albtraum, aus dem es kein Erwachen gibt. Erst patzt Manuel Neuer, dann der Schiedsrichter: Das unglückliche Aus im Halbfinale stürzt den FC Bayern in tiefe Schockstarre. Ein höchst emotionaler Thomas Tuchel schwankt zwischen Trauer, Wut und Verzweiflung. Lachs aus Aquakulturen: »Die Menschen wollen keinen Lachs essen, für den die Umwelt zerstört wird«. In Norwegen wird das Angeln von Wildlachs eingeschränkt, um die Tiere zu schützen. In Kanada sollen Aquakulturen verschwinden, weil sie Ökosysteme zerstören. Wissenschaftler Eirik Biering sagt, was sich bei der Fischzucht ändern muss."
GTEXT3 = """INSERT INTO `meldungen` (`hash`, `datum`, `quelle`, `category`, `titel`, `meldung`, `link`, `status`, `kopiert`) VALUES
(-488858528, '2024-06-24 13:10:33', NULL, 'Politik', 'AfD: Wie wirkt sich die Politik der Partei auf die psychische Gesundheit aus?', 'Hass, Ausgrenzung, falsche Lösungsversprechen: Der Sozialpsychologe Ulrich Sollmann warnt vor dem Aufstieg von Rechtsextremen und Populisten. Die seelische Not vieler Menschen würde dadurch nur verschärft.', NULL, 'kopiert', 0),
(-487421349, '2024-07-15 13:03:00', 'DER SPIEGEL - Schlagzeilen', 'Ausland', 'Lachs aus Aquakulturen: »Die Menschen wollen keinen Lachs essen, für den die Umwelt zerstört wird«', 'In Norwegen wird das Angeln von Wildlachs eingeschränkt, um die Tiere zu schützen. In Kanada sollen Aquakulturen verschwinden, weil sie Ökosysteme zerstören. Wissenschaftler Eirik Biering sagt, was sich bei der Fischzucht ändern muss.', 'https://www.spiegel.de/ausland/lachs-aus-aquakulturen-die-menschen-wollen-keinen-lachs-essen-fuer-den-die-umwelt-zerstoert-wird-a-61d2d4c0-32dc-4510-ac92-1f10c45728cc#ref=rss', 'kopiert', 0),
(-487311596, '2024-06-04 08:17:06', NULL, NULL, 'Nach Attentat in Mannheim: Generalbundesanwalt ermittelt ', 'Die Bundesanwaltschaft hat die Ermittlungen zu dem Attentat in Mannheim übernommen. Grund dafür sei die besondere Bedeutung des Falls. Zugleich werden Forderungen nach einem härteren Vorgehen gegen Islamisten lauter.', NULL, 'kopiert', 0),
(-486042525, '2024-06-08 12:17:04', NULL, NULL, 'Thermische Verhütung: Ring frei für unbeschwerten Sex', 'Eine wachsende Zahl junger Männer möchte Frauen bei der Verhütung entlasten – sie setzen auf einen Ring, der die Hoden erwärmt. Der angehende Gynäkologe Marius Pouplier-von Bonin ist einer von ihnen. Wie fühlt er sich damit?', NULL, 'kopiert', 0),
(-485134084, '2024-06-01 06:17:05', NULL, NULL, 'Qualifikation zur Fußball-EM: Anti-Israel-Demonstrant kettet sich in Glasgow an Torpfosten', 'Zwischenfall beim Auswärtsspiel von Israels Fußballerinnen: Im schottischen Glasgow stürmte ein Mann für eine Protestaktion den Platz – dabei fand das Spiel bereits ohne Zuschauer statt.', NULL, 'kopiert', 0),
(-485076195, '2024-06-02 14:17:04', NULL, NULL, 'Rätsel der Woche: Der Würfeltrick', 'Drei Würfel werden geworfen, Augen addiert und ein Würfel noch mal geworfen. Die Zauberin darf erst am Ende hinschauen, kennt aber trotzdem die Summe. Warum?', NULL, 'kopiert', 0),
(-483893578, '2024-06-26 09:08:18', NULL, 'Panorama', 'Rügen: 75-jähriger Taucher tot am Strand von Nonnevitz gefunden', 'Seine Tauchgruppe hatte ihn kurz zuvor als vermisst gemeldet: Ein Mann ist in Mecklenburg-Vorpommern ums Leben gekommen. Es handelt sich wohl nicht um ein Verbrechen.', NULL, 'kopiert', 0),
(-483628330, '2024-05-28 14:17:07', NULL, NULL, 'Cyril Ramaphosa: Präsident in der Defensive', 'Südafrikas Präsident Ramaphosa glaubt fest an eine Wiederwahl. Doch er hat viele Kritiker und Gegner, auch innerhalb seiner Partei. Wird er auch nach der Präsidentschaftswahl weiter um sein Amt kämpfen müssen? Von S. Ueberbach.', NULL, 'kopiert', 0),"""


def main(Dbg):
    aus = Template(
        """
---------------------------------
>>>   Geheimtext
    $laenge Zeichen
    $h1 unterschiedliche Zeichen
    Leerzeichen $leerz 
    Klein- / Großbuchstaben $lower / $upper
    Ziffern $digit
    Satzzeichen $punkt
    Whitespace $whitespace

    Koinzidenz-Index $koinzidenz % (Erwartungswert $koi2 %)
    (Richtwerte: deutsch: 7,8%, englisch: 6,5%, zufällig: 3,8%)
---------------------------------
    """
    )
    l_text, h1, n_h1, leerz, lower, upper, digit, punkt, whitespace = hauf1(GTEXT3)
    leerz = vorhanden(leerz)
    lower, upper, digit, punkt, whitespace = (
        vorhanden(lower),
        vorhanden(upper),
        vorhanden(digit),
        vorhanden(punkt),
        vorhanden(whitespace),
    )

    sum_hxh1 = sum_pxp = 0
    for zeichen in h1:
        h = h1[zeichen]
        p = h / l_text
        sum_hxh1 += h * (h - 1)
        sum_pxp += p * p
    N = l_text
    koinzidenz = sum_hxh1 / (N * (N - 1))

    print(
        aus.substitute(
            koinzidenz=round(koinzidenz * 100, 2),
            koi2=round(sum_pxp * 100, 2),
            laenge=l_text,
            h1=n_h1,
            leerz=leerz,
            lower=lower,
            upper=upper,
            digit=digit,
            punkt=punkt,
            whitespace=whitespace,
        )
    )
    print("Häufigkeitstabelle:")
    for zeichen in sorted(h1.keys()):
        print(f"{zeichen}: {h1[zeichen]}")


def vorhanden(zeichen):
    if zeichen:
        return "vorhanden"
    else:
        return "keines"


if __name__ == "__main__":
    import argparse, sys, logging

    # ------------------------------------------------------------
    # Parser-Objekt erstellen
    parser = argparse.ArgumentParser(description=DESCRIPTION, epilog=VERSION)
    # ------------------------------------------------------------
    # Übergabe mit Position
    # parser.add_argument('pNumber', type=int, help='Eine Zahl')
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

    # ------------------------------------------------------------
    # Programm aufrufen
    main(Dbg)
