#Tämä koodi pyytää antamaan vuosiluvun ja kertoo onko se karkausvuosi

vuosi = int(input("Insert year: "))

if (vuosi % 400 == 0) and (vuosi % 100 == 0):
    print("{0} is a leap year".format(vuosi))
elif (vuosi % 4 ==0) and (vuosi % 100 != 0):
    print("{0} is a leap year".format(vuosi))
else:
    print("{0} is not a leap year".format(vuosi))