def translate(text):
    def translate_word(word):
        match True:
            # Rule 1: Starts with a vowel, "xr", or "yt"
            case _ if word[0] in "aeiou" or word.startswith(("xr", "yt")):
                return word + "ay"
            case _:
                index = 0
                while index < len(word):
                    # Rule 3: Handle "qu" after zero or more consonants
                    if word[index:index + 2] == "qu":
                        index += 2
                        break
                    # Rule 2 and Rule 4: Stop at a vowel or "y"
                    match word[index]:
                        case "a" | "e" | "i" | "o" | "u":
                            break
                        case "y" if index > 0:
                            break
                        case _:
                            index += 1
                return word[index:] + word[:index] + "ay"
    return " ".join(translate_word(word) for word in text.split())