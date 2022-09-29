
import math

def trailing_zeros(n):
    five_counts = 0
    div = 5
    while div <= n:
        five_counts += math.floor(n/div)
        div *= 5
        
    return five_counts
    
print(trailing_zeros(37))