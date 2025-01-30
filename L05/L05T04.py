def get_fuel(km,kk):
    return "%.1f" % (km / (100 / kk)) + ' ' + "ltr"

print(get_fuel(100,7.5))
print(get_fuel(220,6.9))