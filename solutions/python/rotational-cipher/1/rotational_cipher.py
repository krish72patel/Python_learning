def rotate(text, key):
    result = ""
    for char in text:
        if 'a' <= char <= 'z':
            result += chr((ord(char) - ord('a') + key) % 26 + ord('a'))
        elif 'A' <= char <= 'Z':
            result += chr((ord(char) - ord('A') + key) % 26 + ord('A'))
        else:
            result += char
    return result