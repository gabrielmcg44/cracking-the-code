# generic case ("a", "b", "c", ...)

def pattern_match(value, pattern, pattern_values=None, value_idx=0, pattern_idx=0):

    if value_idx == len(value) and pattern_idx == len(pattern):
        return True

    if value_idx == len(value):
        return False

    if pattern_idx == len(pattern):
        return False

    if type(value) != list:
        value = list(value)

    if type(pattern) != list:
        pattern = list(pattern)

    if pattern_values is None:
        pattern_values = {}

    if pattern[pattern_idx] not in pattern_values.keys():
        for i in range(value_idx, len(value)):
            pattern_values[pattern[pattern_idx]] = [value_idx, i + 1]
            if pattern_match(value, pattern, pattern_values=pattern_values, value_idx=i+1, pattern_idx=pattern_idx+1):
                return True

        pattern_values.pop(pattern[pattern_idx])
        return False

    pattern_value = pattern_values[pattern[pattern_idx]]
    if value_idx + pattern_value[1] - pattern_value[0] > len(value):
        return False

    for i in range(pattern_value[1] - pattern_value[0]):
        if value[pattern_value[0] + i] != value[value_idx + i]:
            return False

    return pattern_match(value, pattern, pattern_values=pattern_values,
                         value_idx=value_idx + pattern_value[1] - pattern_value[0], pattern_idx=pattern_idx + 1)


print(pattern_match(
    "catcatcatcatcatcatcatcatcatcatcatcatcatcatcatcatcatcatcatcatcatcatcatcatcatcatcatcatcatcatcatcatcatcatcatcatcatcatcatcatcatcatcatcatcatcatcatcatgogo",
    "aabb"
))
