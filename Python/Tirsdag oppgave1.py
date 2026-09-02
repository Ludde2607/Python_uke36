alder = int(input("Hvor gammel er du? "))

if alder < 6:
    print("Fordi du er under 6 år gammel slipper du inn gratis")
elif 6 <= alder <= 17:
    print("Din bilett koster 50kr.")
elif 18 <= alder <= 66: 
    print("Din bilett koster 100kr.")
    if alder < 30:
        student = input("Er du student? (ja,Ja,nei,Nei)")
        if student == "ja" or student == "Ja" :
            print("Da sparer du 30 prosent.")
            print("Din nye pris er 70kr.")
        elif student == "nei" or student == "Nei":
            print("Da får du dessvere ikke noe rabatt.")
        else :
            print("Du skrev feil, uflaks. 101kr")
else :
    print("Din bilett koster 50kr.")

