
def multiplies_and_divide(expression, start, end):
    if end == 0:
        return 0

    if end == start:
        raise "Invalid expression"

    operators = {"*", "/"}
    if expression[end - 1] in operators:
        raise "Invalid expression"

    numerator = 1
    denominator = 1

    last_operator_and_index = ["*", start-1]
    for i in range(start, end):
        if expression[i] in operators or i == end-1:
            if i == end - 1:
                i = end
            if last_operator_and_index[1] == i - 1:
                raise "Invalid expression"
            if last_operator_and_index[0] == "*":
                numerator *= float("".join(expression[last_operator_and_index[1]+1:i]))
            if last_operator_and_index[0] == "/":
                denominator *= float("".join(expression[last_operator_and_index[1]+1:i]))
            if i < len(expression):
                last_operator_and_index = [expression[i], i]

    return numerator / denominator


def calculator(expression):
    expression = list(expression)
    signs = {"+", "-"}
    operators = {"+", "-", "*", "/"}

    if expression[len(expression) - 1] in operators:
        raise "Invalid expression"

    sum = 0
    last_sign_and_index = [1, -1]
    for i in range(len(expression)):
        if expression[i] in signs or i == len(expression)-1:
            if i == len(expression)-1:
                i += 1
            sum += last_sign_and_index[0] * multiplies_and_divide(expression, last_sign_and_index[1] + 1, i)

            if i < len(expression):
                last_sign_and_index = [1, i] if expression[i] == "+" else [-1, i]

    return sum


print(calculator("2-6-7*8/2+5"))
