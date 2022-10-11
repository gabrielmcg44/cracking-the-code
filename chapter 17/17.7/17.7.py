
def real_frequencies(names, synonyms):
    real_names = {}
    for synonym in synonyms:
        real_name = [synonym[0]]
        if synonym[0] in real_names.keys() and synonym[1] in real_names.keys():
            real_names[synonym[1]][0] = real_names[synonym[0]][0]
        else:
            if synonym[0] in real_names.keys():
                real_name = real_names[synonym[0]]
            if synonym[1] in real_names.keys():
                real_name = real_names[synonym[1]]

            real_names[synonym[0]] = real_name
            real_names[synonym[1]] = real_name

    real_frequencies_dict = {}
    for name in names:
        real_name = name[0] if name[0] not in real_names.keys() else real_names[name[0]][0]
        if real_name not in real_frequencies_dict.keys():
            real_frequencies_dict[real_name] = 0

        real_frequencies_dict[real_name] += name[1]

    return [[key, real_frequencies_dict[key]] for key in real_frequencies_dict.keys()]


# names = [["John", 15], ["Jon", 12], ["Johnny", 3], ["Johnie", 10], ["Chris", 13], ["Kris", 4], ["Christopher", 19]]
# synonyms = [["Jon", "John"], ["Johnny", "Johnie"], ["John", "Johnny"], ["Chris", "Kris"], ["Chris", "Christopher"]]

names = [["John", 10], ["Jon", 3], ["Davis", 2], ["Kari", 3], ["Johnny", 11], ["Carlton", 8], ["Carleton", 2], ["Jonathan", 9], ["Carrie", 5]]
synonyms = [["Jonathan", "John"], ["Jon", "Johnny"], ["Johnny", "John"], ["Kari", "Carrie"], ["Carleton", "Carlton"]]

print(real_frequencies(names, synonyms))
