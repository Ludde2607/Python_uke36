starttall = int(input("Hva vill du at start tallet skal være? "))
slutttall = int(input("Hva vill du at slutt tallet skal være? "))
steg = int(input("Hvor mange tall vill du den skal hoppe over mellom vært tall? "))
sum_tall = 0
sum_sum_tall = 0
riktig_starttall = starttall / steg
riktig_slutttall = slutttall / steg
for tall in range(int(riktig_starttall), int(riktig_slutttall) +1):
    sum_tall = sum_tall + (tall * steg) 
    print(tall * steg, ": ", sum_tall)
    sum_sum_tall = sum_sum_tall + sum_tall

print(sum_sum_tall)
    

