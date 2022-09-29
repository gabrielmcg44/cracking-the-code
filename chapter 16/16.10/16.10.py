
import math


def radix_sort(int_array):
    max_value = max(int_array)
    digits = 0
    while math.pow(10, digits) <= max_value:
        digits += 1

    current_array = [value for value in int_array]

    for k in range(digits):
        groups = [[], [], [], [], [], [], [], [], [], []]

        for n in current_array:
            groups[math.floor(n/(math.pow(10, k))) % 10].append(n)

        current_array = [item for group in groups for item in group]

    return current_array


def year_most_alive(people_dates):
    years_diffs = {}

    for birth_death in people_dates:
        if birth_death[0] not in years_diffs.keys():
            years_diffs[birth_death[0]] = 1
        else:
            years_diffs[birth_death[0]] += 1

        if birth_death[1] + 1 not in years_diffs.keys():
            years_diffs[birth_death[1] + 1] = -1
        else:
            years_diffs[birth_death[1] + 1] -= 1

    sorted_years = radix_sort(years_diffs.keys())
    num_alive, max_alive = 0, 0
    year_max_alive = None
    for year in sorted_years:
        num_alive += years_diffs[year]
        if num_alive > max_alive:
            max_alive = num_alive
            year_max_alive = year

    return year_max_alive


people_dates = [
    [1805, 1972],
    [1973, 2037],
    [1920, 2000],
    [1950, 2010],
    [1973, 2043],
    [1856, 1945]
]

print(year_most_alive(people_dates))
