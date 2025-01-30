#Tämä näyttää tuumat senttimetreinä

def show_cm(inch):
    cm = inch * 2.54
    return f"{inch} tuumaa on {cm} cm"

print(show_cm(2))
print(show_cm(4.5))
print(show_cm(12))