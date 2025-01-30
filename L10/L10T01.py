#Tämä koodi pyytä syntymävuottasi ja kertoo mihin ikäryhmään kuulut

from datetime import datetime
now = datetime.today()
SV = int(input("Kerro syntymävuotesi: "))
age = now.year - SV

def kerro3(age):
    if age < 1:
        return "Baby"
    elif age < 13:
        return "Child"
    elif age < 19 and age > 13:
        return "Teen"
    elif age > 20 and age < 65:
        return "Adult"
    else:
        return "Senior"

print(kerro3(age))