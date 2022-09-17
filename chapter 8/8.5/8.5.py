#    10100
#     1001
#     ----
#    10100
#   00000
#  00000
# 10100
 
def multiply(a, b):  
    sum = a if b & 1 == 1 else 0
        
    if b == 1:
        return sum
    
    return sum + multiply(a << 1, b >> 1)
    
print(multiply(1,10))