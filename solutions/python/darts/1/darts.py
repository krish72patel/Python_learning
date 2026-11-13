def score(x, y):
    dart = ((x ** 2) + (y ** 2)) ** 0.5
    if dart > 10:
        return 0
    if dart > 5:
        return 1
    if dart > 1:
        return 5
    if dart >= 0:
        return 10
        