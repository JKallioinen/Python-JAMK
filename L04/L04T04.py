luku = 1
num = int (input("Anna numero väliltä 1-10: "))

for luku in range(num):
    luku += 1
    neliö = luku * luku
    print(f"Luvun {luku} neliö on {neliö} ")