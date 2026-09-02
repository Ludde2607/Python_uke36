tall1 = int(input("Gi meg ett tall: "))
tall2 = int(input("GI meg ett tall til: "))
sum = tall1 + tall2
diff = tall1 - tall2
produkt = tall1 * tall2
gjennomsnitt = sum / 2
print("Det blir ", sum, " tilsammen!")

if diff > 0:
    print("De tallene har en forskjell på ", diff, "!")
else:
    ny_diff = diff * -1
    print("De tallene har en forskjell på ", ny_diff, "!")

print("Hvis du ganger de to tallene sammen får du: ", produkt, "!")

print("De har et gjennomsnitt på ", gjennomsnitt, "!")



