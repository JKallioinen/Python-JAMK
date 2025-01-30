class Human:
    name = ""
    age = ""
    def __str__(self):
        return self.name + self.age

person = Human()
person.name = "Adam"
person.age = "19"

person2 = Human()
person2.name = "Eva"
person2.age = "18"

print("Nimi:", person.name + ",", "Ikä:", person.age)
print("Nimi:", person2.name + ",", "Ikä:", person2.age)