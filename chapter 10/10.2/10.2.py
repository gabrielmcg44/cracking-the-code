

def group_anagrams(string_array):
    anagrams_dict = {}
    for base_string in string_array:
        anagram_identifier = "".join(sorted(base_string))
        if anagram_identifier not in anagrams_dict:
            anagrams_dict[anagram_identifier] = []
        
        anagrams_dict[anagram_identifier].append(base_string)
        
    output = []
    for key in anagrams_dict.keys():
        output.extend(anagrams_dict[key])
    
    for i in range(len(output)):
        string_array[i] = output[i]



string_array = ["abc", "abd", "cba", "cbe", "eba", "aec", "aeb", "bce"]

group_anagrams(string_array)

print(string_array)



