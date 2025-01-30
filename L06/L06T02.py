# Celsius -> Farenheit
# Farenheit -> Celsius

def celToFah(C):
    return "%.1f" % ((C * 1.8) + 32)

def fahToCel(F):
    return "%.1f" % ((F - 32) * .5556)

print(celToFah(10.0))
print(fahToCel(38.0))