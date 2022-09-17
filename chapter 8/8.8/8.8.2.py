
memo_split_ways = {}

def get_all_split_ways(target_sum, array_size):
    key = str([target_sum, array_size])
    if key in memo_split_ways.keys():
        return memo_split_ways[key]
    
    if array_size == 1:
        return [[target_sum]]
        
    all_sums = []
    for i in range(target_sum + 1):
        for sum in get_all_split_ways(target_sum - i, array_size - 1):
            new_sum = [ value for value in sum ]
            new_sum.append(i)
            all_sums.append(new_sum)
            
    memo_split_ways[key] = all_sums
    return all_sums
    
def merge_strings(base_str, first_letter, split_way, final_str_size):
    new_permutation = ""
    permutation_index = first_letters_index = 0
    current_split_remaining = split_way[0]
    while permutation_index + first_letters_index < final_str_size:
        if current_split_remaining == 0:
            new_permutation += first_letter
            first_letters_index += 1
            current_split_remaining = split_way[first_letters_index]
        else:
            new_permutation += base_str[permutation_index]
            permutation_index += 1
            current_split_remaining -= 1
    
    return new_permutation

def permute_with_dups(dups_str, starting=True):
    size_str = len(dups_str)
    if size_str <= 1:
        return [dups_str]
    
    if starting:
        dups_str = sorted(dups_str)
        
    change_letter_index = 1
    while dups_str[change_letter_index] == dups_str[0]:
        change_letter_index += 1

    if change_letter_index == size_str:
        return [dups_str]
            
    permutations_no_first_letters = permute_with_dups(dups_str[change_letter_index:], False)

    permutations = []
    first_letter = dups_str[0]
    
    for permutation in permutations_no_first_letters:
        for split_way in get_all_split_ways(size_str - change_letter_index, change_letter_index + 1):
            permutations.append(merge_strings(permutation, first_letter, split_way, size_str))

    return permutations
    

print(permute_with_dups("abca"))
