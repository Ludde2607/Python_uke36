import random

stjerne = ""

def si_hei_til(navn):
    hilsener = ["Hei", "Hallo", "God morgen"]
    print(random.choice(hilsener), navn)

def tegn_katt():
    print("=^.^=")

def navneskilt(navn, star, max_lengde):
    lengde = len(navn)
    for i in range(lengde, max_lengde):
        star += "*"
    return star    


navn = input("Hva heter du? ")
max_lengde = 10






si_hei_til(navn)
tegn_katt()

stjerne = navneskilt(navn, stjerne, max_lengde)
print("*****************")
print(f"{stjerne}{navn}{stjerne}")
print("*****************")

