
x = True
min_liste = []

def p_listen(min_liste):
    print("Din liste er:")
    y = 0
    for i in range(1, len(min_liste) + 1):
        print(y +1 , min_liste[y])
        y +=1
    return min_liste

def fyll_paa(min_liste):
    #For at du skal kunne lette til flere ting fra listen uten å måtte gå inn i "fylle" vær gang
    fyll = True
    while fyll == True:
        oppgave = input("Hva må gjøres? (skriv ferdig når ferdig) ")
        if oppgave == "ferdig" or oppgave == "Ferdig":
            fyll = False
        else:
            min_liste.append(oppgave)

    p_listen(min_liste)
    return min_liste

def fjerne(min_liste):
    #For at du skal kunne fjerne flere ting fra listen uten å måtte gå inn i "fjerne" vær gang
    fjern = True
    while fjern == True:
        ta_bort = input("Hva vill du fjerne fra listen? (skriv ferdig når ferdig) ")
        if ta_bort == "ferdig" or ta_bort == "Ferdig":
            fjern = False
        else:
            y = 0
            for i in range(1, len(min_liste) + 1):
                if min_liste[y] == ta_bort:
                    min_liste.pop(y)
                elif y < len(min_liste):
                    y +=1
                else:
                    print("Det fant jeg ikke på listen, prøv igjen og se om du skrev det riktig.")

    p_listen(min_liste)

#For å få den til å kjøre hele tiden
while x == True:

    gjøre = input("Vill du fylle på eller ferne gjøremål fra listen? (skriv fylle, fjerne eller listen) ")

    if gjøre == "fylle" or gjøre == "Fylle":
        fyll_paa(min_liste)
    elif gjøre == "fjerne" or gjøre == "Fjerne":
        fjerne(min_liste)
    elif gjøre == "listen":
        p_listen(min_liste)
    elif gjøre == "stop":
        #For å stopp programmet
        x = False
    else:
        print("Det kan jeg ikke gjøre")
    