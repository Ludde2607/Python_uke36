tall = int(input("Hvilken gangetabell? "))
lengde = int(input("Hvor lang vill du at den skal være? "))
for i in range(1,lengde+1):
    print(tall, "x", i, "=", tall * i)
