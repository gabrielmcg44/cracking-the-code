# 1^0|0|1        false

# (1)^((0)|((0)|(1)))

from itertools import count


memo_counts = {}

def count_eval(expression, result):
    expression_len = len(expression)
    if expression_len == 1:
        if (result and expression == "1") or (not result and expression == "0"):
            return 1
        return 0
    
    key = str([expression, result])
    if key in memo_counts.keys():
        return memo_counts[key]
        
    num_operators = int((expression_len - 1)/2)
    count_ways = 0
    for i in range(num_operators):
        operator = expression[1 + 2*i]
        left_side = expression[:1+2*i]
        right_side = expression[2*(i+1):]
        if operator == "&" and result:
            count_ways += count_eval(left_side, result)*count_eval(right_side, result)
        if operator == "&" and not result:
            count_ways += count_eval(left_side, result)*count_eval(right_side, result)
            count_ways += count_eval(left_side, not result)*count_eval(right_side, result)
            count_ways += count_eval(left_side, result)*count_eval(right_side, not result)
        if operator == "|" and result:
            count_ways += count_eval(left_side, result)*count_eval(right_side, result)
            count_ways += count_eval(left_side, not result)*count_eval(right_side, result)
            count_ways += count_eval(left_side, result)*count_eval(right_side, not result)
        if operator == "|" and not result:
            count_ways += count_eval(left_side, result)*count_eval(right_side, result)
        if operator == "^" and result:
            count_ways += count_eval(left_side, not result)*count_eval(right_side, result)
            count_ways += count_eval(left_side, result)*count_eval(right_side, not result)
        if operator == "^" and not result:
            count_ways += count_eval(left_side, result)*count_eval(right_side, result)
            count_ways += count_eval(left_side, not result)*count_eval(right_side, not result)
    
    memo_counts[key] = count_ways
    return count_ways

print(count_eval("0&0&0&1^1|0", True))