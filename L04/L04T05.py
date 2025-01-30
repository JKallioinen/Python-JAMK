etunimi = input("Anna etunimesi: ")
sukunimi = input("Anna sukunimesi: ")

eka = etunimi[0]
pituus = len(etunimi)
snimi = ''.join(reversed(sukunimi))
print(eka*pituus, snimi)