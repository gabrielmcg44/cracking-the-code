
import sys

def smallest_difference(arr_1, arr_2):
    len_1 = len(arr_1)
    len_2 = len(arr_2)
    
    if len_1*len_2 == 0:
        return -1
        
    sorted_1 = sorted(arr_1)
    sorted_2 = sorted(arr_2)

    counter_1 = 0
    counter_2 = 0
    
    min_diff = sys.float_info.max
    
    while counter_1 < len_1 and counter_2 < len_2:
        min_diff = min(min_diff, abs(sorted_1[counter_1] - sorted_2[counter_2]))
        
        if sorted_1[counter_1] > sorted_2[counter_2]:
            counter_2 += 1
        else:
            counter_1 += 1
    
    return min_diff
  

arr_1 = [1, 7, 18, 29, 35, 49, 53]
arr_2 = [13, 25, 32, 43]

print(smallest_difference(arr_1, arr_2))