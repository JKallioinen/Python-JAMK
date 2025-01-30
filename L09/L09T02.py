#Tämä koodi näyttää nimet tehtävästä L09T01 sekä annetussa että aakkosjärjestyksessä

filename = "names.txt"
file = open(filename, "r")
names = file.readlines()
print(names)
names.sort()
print(names)
file.close()