def is_armstrong_number(number):
    result = 0
    temp_num = number
    power = len(str(number))

    while temp_num:
        digit = temp_num % 10
        result += digit ** power
        temp_num //= 10

    return number == result