filename = "lotto.txt"
file = open(filename, "w")
import random
lottorivit = {}
x = int(input("Montako riviä arvotaan?: "))
for rivi in range(x):
    lottorivi = random.sample(range(1, 40), 7)
    file.write(str(lottorivi) + "\n")
    #print(ok)
file.close()