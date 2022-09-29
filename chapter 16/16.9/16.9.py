
def negate(a):
    signs = [1, -1] if a > 0 else [-1, 1]
    curr, result = 0, 0
    while curr != a:
        curr += signs[0]
        result += signs[1]

    return result


def subtract(a, b):
    return a + negate(b)


def multiply(a, b):
    sign = 1
    if a < 0:
        sign = negate(sign)
        a = negate(a)

    if b < 0:
        sign = negate(sign)
        b = negate(b)

    result = 0
    for _ in range(b):
        result += a

    return result if sign == 1 else negate(result)


def divide(a, b):
    if b == 0:
        return None

    sign = 1
    if a < 0:
        sign = negate(sign)
        a = negate(a)

    if b < 0:
        sign = negate(sign)
        b = negate(b)

    result = 0
    curr = b
    while curr <= a:
        curr += b
        result += 1

    return result if sign == 1 else negate(result)


print(subtract(5, 2))
print(multiply(-5, -2))
print(divide(0, 4))
