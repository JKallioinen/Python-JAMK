#Anna 5 lukua väliltä 1-20
#Tämä koodi laskee niistä yhteen kaikki muut luvut, paitsi suurimman ja pienimmän luvun

points = []
total = 0
for point in range(5):
    point = int(input("Hypyn pisteet: "))
    points.append(point)
points.remove(min(points))
points.remove(max(points))
for point in points:
    total += point
print("Pisteet yhteensä: ", total)