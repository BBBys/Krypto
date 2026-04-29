#Textausgabe in Fünfergruppen mit Zeilenumbruch nach b Zeichen
def print5(text,gruppe=5,zeile=70):
    länge=0
    for i in range(0, len(text), gruppe):
        ausgabe=str(text[i : i + gruppe])
        print(ausgabe, end=" ")
        länge+=len(ausgabe)+1
        if länge> zeile:   
            print()
            länge=0
    print() 