# 10 autoa järjestetty rekisterinumeron mukaan
# 2 tapaa
# jälkimmäinen tapa -> selkeämpi lopputulos

register_plates = {
    "ABC-123": "Skoda",
    "ABC-234": "Audi",
    "BCD-123": "Fiat",
    "CDE-234": "Renault",
    "CDE-456": "Mercedes",
    "ABC-567": "Skoda",
    "RBC-432": "Audi",
    "BGD-352": "Nissan",
    "CEE-724": "Porche",
    "CDT-472": "Kia",
}
#print(sorted(register_plates.items()))

for plate, brand in sorted(register_plates.items()):
    print(plate, brand)