#Tuottaa lottorivin 
import random
def lotto():
    print(*sorted(random.sample(range(1, 40), 7)), sep=",")

lotto()