antall = int(input("Hvor mange har du kjøpt? "))
pris = int(input("Hvor mye koster de? "))
rabatt = int(input("Hvor mange prosent rabatt har du? "))
total_pris = antall * pris
riktig_rabat = rabatt / 100
spart = total_pris * riktig_rabat
ny_pris = total_pris - spart

print("Det ville kostet ", total_pris, ", men siden du har ", rabatt, "prosent rabbat sparer du", spart, "kroner.")
print("Du må betale ", ny_pris, "kroner.")