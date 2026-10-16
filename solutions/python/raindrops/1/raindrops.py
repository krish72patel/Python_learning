def convert(number):
    strin = ""
    if number % 3 == 0:
        strin += "Pling"
    if number % 5 == 0:
        strin += "Plang"
    if number % 7 == 0:
        strin += "Plong"
    if strin == "":
        strin = str(number)
    return strin