#Anna 10 nimeä
#Tämä näyttää ne listana ja käännettynä listana
namelist = []
for name in range(10):
    name = input("Give a name:")
    namelist.append(name)
print(namelist)
namelist.reverse()
print(namelist)