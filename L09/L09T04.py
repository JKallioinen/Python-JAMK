#Tämä koodi kertoo montako nimeä, ja montako kertaa kukin nimi esiintyy tiedostossa nimet.txt

filename = "nimet.txt"
file = open(filename, "r")
nimet = file.readlines()
nimet.sort()

def lukumaarat(lista):
    names = {}
    for name in lista:
        if name not in names:
            names[name] = 0
        names[name] += 1
    return names
print("Nimiä listassa:", len(nimet))
print(lukumaarat(nimet))
file.close()