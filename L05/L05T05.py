# km = kilometrit
# kk = keskikulutus
# lh = litrahinta
def get_fuel(km,kk,lh):
    return "%.2f" % (km / (100 / kk) * lh) + ' ' + "€"

print(get_fuel(100, 7.5, 1.88))
print(get_fuel(220, 6.9, 1.88))