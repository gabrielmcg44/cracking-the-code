
summary = None

def find_num_ocurrences(book, search_word):
    global  summary
    if summary is None:
        summary = {}
        for word in book.lower().split():
            if word in summary.keys():
                summary[word] += 1
            else:
                summary[word] = 1
    
    if search_word in summary.keys():
        return summary[search_word]
    
    return 0
    
phrase = "Era uma vez um livro bem pequeno e sem pontuações lorem ipsum lorem ipsum bla bla bla"

print(find_num_ocurrences(phrase, "bla"))
print(find_num_ocurrences(phrase, "lorem"))
print(find_num_ocurrences(phrase, "pontuações"))
print(find_num_ocurrences(phrase, "ez"))
print(find_num_ocurrences(phrase, "era"))