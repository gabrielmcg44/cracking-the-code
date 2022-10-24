def is_compound_word(word, words_set, start=0):
    if start == len(word):
        return True

    partial = ""
    for i in range(start, len(word)):
        if i == len(word) - 1 and start == 0:
            return False

        partial += word[i]
        if partial in words_set and is_compound_word(word, words_set, i + 1):
            return True

    return False


def longest_word(words_list):
    words_set = set(words_list)
    longest_word = ""
    for word in words_list:
        if is_compound_word(word, words_set) and len(word) > len(longest_word):
            longest_word = word

    return longest_word if longest_word != "" else None


print(longest_word(["cat", "banana", "dog", "nana", "catnanadogmoonwalker", "walk", "walker", "dogwalker", "moon", "moonwalker"]))

