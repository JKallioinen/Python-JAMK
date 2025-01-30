#Anna jokin määrä nimiä
#Tyhjän rivin jälkeen antaa oppilaiden lukumäärän ja listan nimistä

nimet = []
while True:
    nimi = input("Anna oppilaan nimi: ")
    if nimi == '':
        break
    else:
        nimet.append(nimi)

print("Oppilaita: ", len(nimet))
print(*nimet, sep=", ")