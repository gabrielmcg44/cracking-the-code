def letter_to_code(letter):
    if letter in {"a", "b", "c"}:
        return "2"
    elif letter in {"d", "e", "f"}:
        return "3"
    elif letter in {"g", "h", "i"}:
        return "4"
    elif letter in {"j", "k", "l"}:
        return "5"
    elif letter in {"m", "n", "o"}:
        return "6"
    elif letter in {"p", "q", "r", "s"}:
        return "7"
    elif letter in {"t", "u", "v"}:
        return "8"
    elif letter in {"w", "x", "y", "z"}:
        return "9"


def word_to_code(word):
    code = ""
    for letter in word:
        code += letter_to_code(letter)

    return code


def make_code_dict(words):
    code_dict = {}
    for word in words:
        code = word_to_code(word)
        if code not in code_dict.keys():
            code_dict[code] = [word]
        else:
            code_dict[code].append(word)

    return code_dict


code_dict = make_code_dict(["star", "tree", "used", "true", "else", "load", "long", "went", "well", "corn", "them", "uped"])


def suggestions(code):
    if code in code_dict.keys():
        return code_dict[code]

    return []


print(suggestions("8733"))

