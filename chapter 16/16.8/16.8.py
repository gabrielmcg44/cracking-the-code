
import math

zero_nineteen = [
    "zero", "one", "two", "three", "four", 
    "five", "six", "seven", "eight", "nine", 
    "ten", "eleven", "twewlve", "thirteen", "fourteen", 
    "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"
]

ten_multiples = ["twenty", "thirty", "fourty", "fifty", "sixty", "seventy", "eighty", "ninety"]

thousend_powers = ["", "thousend", "million", "billion", "trillion"]

def english_int(number):
    positive = abs(number)
    if positive != number:
        return "minus" + english_int(positive)
    
    if number < 20:
        return zero_nineteen[number]
    
    if number < 100:
        units = "" if number % 10 == 0 else zero_nineteen[number % 10]
        return (ten_multiples[math.floor(number / 10) - 2] + " " + units).strip()
    
    if number < 1000:
        after_hundreds = english_int(number % 100)
        hundreds = zero_nineteen[math.floor(number / 100)] + " " + "hundred"
        return (hundreds + " " + ("" if after_hundreds == "zero" else after_hundreds)).strip()
    
    broke_number = []
    
    while True:
        broke_number.append(number % 1000)
        if number / 1000 < 1:
            break
        number = math.floor(number / 1000)
    
    N = len(broke_number)
    
    phrase = []       
    for i in range(N):
        if broke_number[N-1-i] != 0:
            phrase.append(english_int(broke_number[N-1-i]) + " " + thousend_powers[N-1-i])

    return ", ".join(phrase)
    
        

for i in [
    1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19,
    20, 21, 32, 43, 54, 65, 76, 87, 98, 100, 101, 109, 115, 120, 121,
    175, 189, 201, 202, 250, 378, 1275, 3002, 3000, 30100, 100000, 123456789
]:
    print(i, english_int(i))