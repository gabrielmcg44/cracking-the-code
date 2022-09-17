
counter = 0

def sparse_search(sparse_array, wanted_string, left=0, right=None, right_boundary=None):
    if right is None:
        right = len(sparse_array)
    
    if left > right:
        return -1
    
    if right_boundary is None:
        right_boundary = [right]
    
    global counter
    counter = counter + 1
    
    middle = (left + right) // 2
    if sparse_array[middle] == wanted_string:
        return middle
    elif sparse_array[middle] == "":
        left_index = sparse_search(sparse_array, wanted_string, left, middle-1, right_boundary)
        if left_index != -1:
            return left_index
        
        return -1 if right_boundary[0] < middle + 1 else sparse_search(
            sparse_array, wanted_string, middle + 1, right, right_boundary
        )
    elif sparse_array[middle] < wanted_string:
        return sparse_search(sparse_array, wanted_string, middle + 1, right, right_boundary)
    elif sparse_array[middle] > wanted_string:
        right_boundary[0] = middle - 1
        return sparse_search(sparse_array, wanted_string, left, middle - 1, right_boundary)

sparse_array = ["at", "", "", "", "ball", "", "", "car", "", "", "dad", "", "", "ear", "", "", "", "", "fire", "", "", "goat", "", "", "here", "", "", "i", "", "", "james", "", "", "key", "", "", "long"]

print("array size", len(sparse_array))

print(sparse_search(sparse_array, "dad"))

print("counter:", counter)