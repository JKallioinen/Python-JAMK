luku = int (input("Anna kokonaisluku: "))
luku2 = int (input("Anna toinen kokonaisluku: "))
luku3 = int (input("Anna kolmas kokonaisluku: "))

if (luku > luku2 and luku > luku3):
    print(f"Suurin: {luku} ")
elif (luku2 > luku and luku2 > luku3):
    print(f"Suurin: {luku2} ")
else:
    print(f"Suurin: {luku3} ")