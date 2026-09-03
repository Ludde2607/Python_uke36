import random

def kast_terning():
    return random.randint(1, 6)

def spill(antall_kast):
    par = 0
    syv = 0
    poeng = 0
    

    for tall in range(1, antall_kast + 1):
        terning = kast_terning()
        terning2 = kast_terning()
        sum = terning + terning2

        if terning == terning2:
            par = par + 1
            poeng = poeng + 2
        
        elif sum == 7:
            syv = syv + 1
            poeng = poeng + 1

    print("På", antall_kast, "kast Fikk du", par, "par og", syv, "kast hvor summen ble 7!")
    print("Spiller", spiller, "fikk derfor", poeng, "poeng!")
    return poeng
    
print("Vellkommen til terning spillet")
print("Her kastes 2 terninger så mange ganger dere ønsker!")
print("Et par(2 liker) gir 2 poeng")
print("Hvis summen av terningene blir 7 får du 1 poeng")
antall_spillere = int(input("Hvor mange vill spille? "))
antall_kast = int(input("Hvor mnage kast vill dere at vær spiller skal ha? "))


spiller = 0
top_poeng = 0
ledere = []

for tall in range(1, antall_spillere + 1):
    spiller = spiller + 1
    poeng = spill(antall_kast)
    print(poeng)
    if poeng > top_poeng:
        top_poeng = poeng
        ledere = []
        ledere.append(spiller)
    elif poeng == top_poeng:
        print("flere leder")
        ledere.append(spiller)

print("Spiller", ledere, "vant med", top_poeng , "!")