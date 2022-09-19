
import math

def radix_sort(int_array):
    max_value = max(int_array)
    digits = 0
    while math.pow(10, digits) <= max_value:
        digits += 1
    
    current_array = [value for value in int_array]

    for k in range(digits):
        groups = [[], [], [], [], [], [], [], [], [], []]

        for n in current_array:
            groups[math.floor(n/(math.pow(10, k))) % 10].append(n)
        
        current_array = [item for group in groups for item in group]
    
    return current_array


def peaks_and_valeys(int_array):
    sorted_array = radix_sort(int_array)

    n = len(int_array)
    mid = math.floor((n-1)/2)
    
    index1 = 0
    index2 = math.floor((n-1)/2) + 1
    step = 1
    
    peaks_and_valeys_array = []
    
    while index1 < mid + 1 or index2 < n:
        if step % 2 == 1:
            peaks_and_valeys_array.append(sorted_array[index1])
            index1 += 1
        else:
            peaks_and_valeys_array.append(sorted_array[index2])
            index2 += 1
        
        step += 1
            
    return peaks_and_valeys_array    
    
int_array = [47, 32, 83, 98, 99, 3, 2, 51, 87, 5, 3, 82, 37, 73, 78, 78, 25]

print(peaks_and_valeys(int_array))