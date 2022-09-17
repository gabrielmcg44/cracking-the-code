def permute_with_dups(dups_str):
    size_str = len(dups_str)
    if size_str <= 1:
        return [dups_str]
        
    permutations_no_first = permute_with_dups(dups_str[1:])
    
    permutations = []
    first_letter = dups_str[0]
    
    for permutation in permutations_no_first:
        current_first_letter = False
        for i in range(size_str):
            if not current_first_letter:
                permutations.append((permutation[:i] + first_letter + permutation[i:])) 
            
            if i < size_str - 1:
                current_first_letter = True if permutation[i] == first_letter else False
            
    return permutations
    

print(permute_with_dups("abac"))
print(len(permute_with_dups("abac"))) 

word = {
    "a": 2,
    "b": 1,
    "c": 1
}