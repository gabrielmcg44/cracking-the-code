
import sys

class Listy:
    def __init__(self, normal_list):
        self._list = normal_list
        self._size = len(normal_list)
    
    def element_at(self, i):
        if i < 0 or i >= len(self._list):
            return -1
        
        return self._list[i]
      
  
def find_x(listy, x, left=0, right=None):
    if right is None:
        right = 1
        while (listy.element_at(right) != -1 and listy.element_at(right) < x):  # esqueci a segunda verificação, n tá errado mas demora mais
            right *= 2
    
    if left > right or x < 0:
        return -1
     
    middle = (left + right) // 2
    middle_element = listy.element_at(middle)

    middle_value = middle_element if middle_element != -1 else sys.float_info.max
    if middle_value == x:
        return middle
    
    if x < middle_value:
        return find_x(listy, x, left, middle - 1)
        
    if x > middle_value:
        return find_x(listy, x, middle + 1, right)
      
  
listy = Listy([0, 2, 5, 6, 9, 9, 9, 9, 10, 10, 12, 13, 14, 14, 16, 17])
print(find_x(listy, 11))