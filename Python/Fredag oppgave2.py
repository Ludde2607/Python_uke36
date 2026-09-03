import random

def kast_terning():
    return random.randint(1, 6)

par = 0
syv = 0
kast = int(input("Hvor mange ranger vill du kaste to terninger? "))

for tall in range(1, kast+1):
    terning = kast_terning()
    terning2 = kast_terning()
    sum = terning + terning2

    if terning == terning2:
        par = par + 1
        
    elif sum == 7:
        syv = syv + 1

print("På", kast, "Fikk du", par, "par og", syv, "kast hvor summen ble 7!")
