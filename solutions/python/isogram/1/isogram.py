def is_isogram(phrase):
    letters = []

    for char in phrase.lower():
        if char == ' ' or char == '-':
            continue

        if char in letters:
            return False

        letters.append(char)

    return True