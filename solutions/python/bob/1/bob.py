def response(hey_bob):
    if not hey_bob.strip() :
        return "Fine. Be that way!"
    hey_bob = hey_bob.strip()
    length = len(hey_bob)
    if hey_bob[length - 1] == "?" and hey_bob.isupper():
        return "Calm down, I know what I'm doing!"
    if hey_bob[length - 1] == "?":
        return "Sure."
    if hey_bob.isupper():
        return "Whoa, chill out!"
    return "Whatever."