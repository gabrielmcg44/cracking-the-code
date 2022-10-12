
def max_floors(people):
    people = sorted(people)
    general_max_height = 1
    max_height_by_tops = {}
    for idx in range(len(people)):
        i = len(people) - 1 - idx
        max_height = 1
        for j in range(i+1, len(people)):
            if people[j][1] > people[i][1]:

                max_height = max(max_height, 1 + max_height_by_tops[j])

        general_max_height = max(general_max_height, max_height)
        max_height_by_tops[i] = max_height

    return general_max_height


people = [[65, 90], [70, 150], [56, 90], [75, 190], [60, 95], [68, 110], [80, 190], [77, 140]]
print(max_floors(people))
