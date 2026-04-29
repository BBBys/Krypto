import logging, string


def hauf1(txt):
    hauf = {}
    for zeichen in string.ascii_letters:
        hauf[zeichen] = 0
    leer = lower = upper = digit = punkt = whitespace = False
    for zeichen in txt:
        if zeichen in hauf:
            hauf[zeichen] += 1
        else:
            #neu, ist dann ein Sonderzeichen
            hauf[zeichen] = 1
        # upper/lower hier in txt testen, da in hauf schon alle Zeichen vorliegen
        if not upper and testfor(zeichen, string.ascii_uppercase):
            upper = True
        if not lower and testfor(zeichen, string.ascii_lowercase):
            lower = True

    for zeichen in hauf:
        #die folgenden sind nicht schon vorbelegt
        if not digit and testfor(zeichen, string.digits):
            digit = True
        if not punkt and testfor(zeichen, string.punctuation):
            punkt = True
        if not whitespace and testfor(zeichen, string.whitespace):
            whitespace = True
        if not leer and testfor(zeichen, " "):
            leer = True

    return len(txt), hauf, len(hauf), leer, lower, upper, digit, punkt, whitespace

#ist ein Zeichen Element dieses Zeichensatzes? 
# (z.B. string.digits, string.ascii_uppercase, etc.)
def testfor(zeichen, zeichensatz):
    return zeichen in zeichensatz
