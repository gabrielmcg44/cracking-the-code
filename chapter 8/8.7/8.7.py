

def permute_without_dups(no_dups_str):
    size_str = len(no_dups_str) # erro: economizaria conta
    if size_str <= 1:
        return [no_dups_str]   # era pra ter voltado o vetor
        
    permutations_no_first = permute_without_dups(no_dups_str[1:])
    
    permutations = []
    first_letter = no_dups_str[0]
    
    for permutation in permutations_no_first:
        for i in range(size_str):
            permutations.append((permutation[:i] + first_letter + permutation[i:])) # erro: aprendizado [i:] funciona mesmo se i estiver fora
            
    return permutations
    

print(permute_without_dups("gabriel"))