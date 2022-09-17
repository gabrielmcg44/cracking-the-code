import math

# 4 kbytes = 32000 bits

class BitArray:
    def __init__(self, size):
        self.bits = [0] * math.ceil(size / 32)
        self.size = size
    
    def get(self, index):
        if index > self.size:
            raise "Index not found"
        return self.bits[math.floor(index / 32)] & (1 << ((index - 1) % 32)) != 0
    
    def flip(self, index):
        self.bits[math.floor(index / 32)] ^= (1 << ((index - 1) % 32))
        

def print_duplicates(int_array):
    bit_array = BitArray(32000)
    for i, value in enumerate(int_array):
        if not bit_array.get(value):
            int_array[i] = 0
            bit_array.flip(value)
    
    # wanted to print the duplicate just one time
    for _, value in enumerate(int_array):
        if value != 0 and bit_array.get(value):
            print(value)
            bit_array.flip(value)
            
int_array = [3, 4, 2, 7, 4, 1, 2, 1, 5, 9, 3, 7, 8, 7]

print_duplicates(int_array)