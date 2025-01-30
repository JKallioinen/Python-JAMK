#Anna niin monta sukunimeä kuin haluat
#Tämä tallentaa ne tiedostoon

filename = "names.txt"
file = open(filename, "w")
name = "*"
i = 0
while name != "":
    name = input("Anna sukunimi: ")
    if name != "":
        file.write(name + "\n")
        i += 1
file.close()
file = open(filename, "r")
names = file.readlines()
print(names)
file.close()