import math

def abs_value(number):
    math.sqrt(number^2)

def max_of_two(number_1, number_2):
    return (number_1 + number_2)/2 + abs_value((number_1 - number_2)/2)
    

print(max_of_two(4, 8))