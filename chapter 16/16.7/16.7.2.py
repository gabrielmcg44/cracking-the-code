
def flip(bit):
    return 1^bit

def sign(number):
    return flip((number >> 31) & 1)

def get_max(a, b):
    c = a - b
    
    sa = sign(a)
    sb = sign(b)
    sc = sign(c)
    
    use_sign_of_a = sa ^ sb
    use_sign_of_c = flip(sa ^ sb)
    
    k = use_sign_of_a * sa + use_sign_of_c * sc
    q = flip(k)
    
    return a * k + b * q
    
print(get_max(51, 50))