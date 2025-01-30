class Cat:
    name = ""
    color = ""
    def meow(self):
        return "Meooooooow!"
    def __str__(self):
        return self.name + self.color
    
cat = Cat()
cat.name = "Kit"
cat.color = "Black"

cat2 = Cat()
cat2.name = "Kat"
cat2.color = "white"

print(cat.name + ",", "Color:", cat.color)
print(cat2.name + ",", "Color:", cat2.color)
print(cat.name, "says: ", cat.meow())
print(cat2.name, "says: ", cat2.meow())