
from libcst import Return


def find_in_rotated_array(rotated_array, number, init=0, last=None):
    if last is None:
        last = len(rotated_array) - 1
        
    if init > last:
        return -1
        
    middle = (init + last) // 2
    
    if number == rotated_array[middle]:
        return middle
    
    if rotated_array[init] < rotated_array[middle]: 
        if number < rotated_array[middle] and number >= rotated_array[init]:
            return find_in_rotated_array(rotated_array, number, init, middle - 1)
        return find_in_rotated_array(rotated_array, number, middle + 1, last)
    
    if rotated_array[middle] < rotated_array[last]:
        if number > rotated_array[middle] and number <= rotated_array[last]:
            return find_in_rotated_array(rotated_array, number, middle + 1, last)
        return find_in_rotated_array(rotated_array, number, init, middle - 1)
        
    if rotated_array[middle] == rotated_array[init] and rotated_array[middle] == rotated_array[last]:
        left_index = find_in_rotated_array(rotated_array, number, init, middle - 1)
        return left_index if left_index != -1 else find_in_rotated_array(
            rotated_array, number, middle + 1, last
        )
    
    if rotated_array[middle] == rotated_array[init]:
        return find_in_rotated_array(rotated_array, number, middle + 1, last)
        
    if rotated_array[middle] == rotated_array[last]:
        return find_in_rotated_array(rotated_array, number, init, middle - 1)
        
    return -1
    
    
rotated_array = [2, 2, 2, 3, 4, 2]

print(find_in_rotated_array(rotated_array, 4))