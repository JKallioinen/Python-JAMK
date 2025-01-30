#Muuttaa sekunnit muotoon hh:mm:ss

def show_time(seconds):
    hours = seconds // 3600
    minutes = seconds % 3600 // 60
    seconds = seconds % 3600 % 60
    time = "{:02d}:{:02d}:{:02d}".format(hours, minutes, seconds)
    return time

print("Time: ", show_time(500))
print("Time: ", show_time(10000))
print("Time: ", show_time(121000))