#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Wichtig:
# export PYTHONPATH="../FLElib"
#

import logging, string


def KrVorbereitung(text):
    text = text.upper()
    for c in string.punctuation + string.whitespace + string.digits:
        text = text.replace(c, "")
    text = (
        text.replace("Ä", "AE").replace("Ö", "OE").replace("Ü", "UE").replace("ß", "SS")
    )

    for c in text:
        if c not in string.ascii_uppercase:
            logging.debug(f"Zeichen '{c}' entfernt")
            text = text.replace(c, "")

    return text
