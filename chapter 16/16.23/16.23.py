
import random


def rand_5():
    return random.randint(0, 4)


def rand_2():
    rand5 = rand_5()
    if rand5 < 2:
        return 0
    if rand5 > 2:
        return 1
    return rand_2()


def rand_7():
    rand8 = rand_2() * 1 + rand_2() * 2 + rand_2() * 4
    if rand8 != 7:
        return rand8

    return rand_7()


print(rand_5())

counts = [0]*7
for _ in range(700000):
    counts[rand_7()] += 1

print(counts)


