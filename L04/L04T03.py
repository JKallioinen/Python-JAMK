x = 0
z = 0
while True:
    try:
        y = int (input("Anna luku: "))
        x += 1
        z += y
    except ValueError:
        break
print("Lukuja annettu: ", x)
print("Lukujen summa: ", z)