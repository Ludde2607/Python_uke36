import random

def kast_terning():
    return random.randint(1, 6)

terning = kast_terning()
terning2 = kast_terning()

print(terning)
print(terning2)

sum = terning + terning2

print(sum)

if terning == terning2:
    print("Begge terningene viser", terning, "!")
    print("Summen ble", sum, "!")
elif sum == 7:
    print("Ojj det ble 7 tilsammen!")
else:
    print("Summen ble", sum, "!")