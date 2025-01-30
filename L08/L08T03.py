#Anna haluamasi määrä arvosanoja väliltä 0-5
#Tämä laskee annettujen arvosanojen määrän ja keskiarvon
list = []
sum = 0
while True:
    arvosana = input("Anna arvosana väliltä 0-5: ")
    if arvosana == "":
        break
    else:
        list.append(arvosana)
        sum += int(arvosana)
print("Arvosanoja annettu: ", len(list))
average = sum / len(list)
print("Arvosanojen keskiarvo: ""%.2f" % average)