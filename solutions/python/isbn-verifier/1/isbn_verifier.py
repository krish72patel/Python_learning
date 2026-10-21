def is_valid(isbn):
    isbn = isbn.replace("-", "")

    if len(isbn) != 10:
        return False
        
    if not isbn[:9].isdigit():
        return False

    if not (isbn[9].isdigit() or isbn[9] == "X"):
        return False

    digits = [int(char) for char in isbn[:9]]
    digits.append(10 if isbn[9] == "X" else int(isbn[9]))

    total = sum(digit * weight for digit, weight in zip(digits, range(10, 0, -1)))

    return total % 11 == 0