#Anna haluamasi määrä rekisterinumeroita
#Tämä tulostaa ne listana aakkosjärjestyksessä
#Lopussa on vaihtoehtona vähemmän siisti lista
reg_plates = []
while True:
    plate = input("Give a plate number:")
    if plate == "":
        break
    else:
        reg_plates.append(plate)
reg_plates.sort()
for plates in reg_plates:
    print(plates)
#print(reg_plates)