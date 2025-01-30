#Tämä kysyy lukuja, tyhjä syöte lopettaa.
#Lopuksi ohjelma kertoo montako lukua annettu ja näyttää annetut luvut

filename = "luvut.txt"
file = open(filename, "w")
luku = "*"
i = 0
while luku != "":
    luku = input("Anna kokonaisluku: ")
    if luku != "":
        file.write(luku + "\n")
        i += 1
file.close()
file = open(filename, "r")
luvut = file.readlines()
print("Lukuja annettu: ", i)
print(luvut)
file.close()