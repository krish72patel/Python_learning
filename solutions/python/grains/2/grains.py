def square(number):
    if number > 64 or number < 1 :
        raise ValueError("square must be between 1 and 64")
    count = 1
    grains = 1
    while (count < number):
        grains *= 2
        count += 1
    return grains

def total():
    number = 1
    total = 1
    count = 1 
    while (number < 64) :
        total += count * 2
        count = count * 2
        number += 1
    return total