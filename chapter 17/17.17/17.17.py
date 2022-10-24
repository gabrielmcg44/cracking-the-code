def build_trie(dictionary):
    trie = {}
    for word in dictionary:
        root = trie
        for letter in word:
            if letter not in root.keys():
                root[letter] = {}

            root = root[letter]

        root["end"] = True

    return trie


def find_words(b, T):
    trie = build_trie(T)
    markers = {}
    found_words = []
    for i in range(len(b)):
        markers[str(i)] = trie
        for key in list(markers.keys()):
            if b[i] not in markers[key].keys():
                del markers[key]
                continue

            markers[key] = markers[key][b[i]]
            if "end" in markers[key].keys():
                found_words.append([int(key), int(i)])

    return found_words


T = ["looked", "just", "like", "her", "brother", "here", "i", "is", "island", "insane", "ertimis"]
b = "jesslookedjustlikeherbrothertimisland"

print(find_words(b, T))
