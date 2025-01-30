point = int(input("Pisteet: "))

if (point <= 0 or point == 1):
    print("Arvosana: 0")
elif (point == 2 or point == 3):
    print("Arvosana: 1")
elif (point == 4 or point == 5):
    print("Arvosana: 2")
elif (point == 6 or point == 7):
    print("Arvosana: 3")
elif (point == 8 or point == 9):
    print("Arvosana: 4")
elif (point == 10 or point == 11 or point == 12):
    print("Arvosana: 5")
else:
    print("ERROR: Too many points!")