# Koinzidenz-Index
def koiIx(häufigkeiten, nToken):
    sum_hxh1 = 0
    sum_pxp = 0

    for zeichen in häufigkeiten:
        absHäufType = häufigkeiten[zeichen]
        relHäufType = absHäufType / nToken
        sum_hxh1 += absHäufType * (absHäufType - 1)
        sum_pxp += relHäufType * relHäufType

    koinzidenz = sum_hxh1 / (nToken * (nToken - 1))

    return koinzidenz
