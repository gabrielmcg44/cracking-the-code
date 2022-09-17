
def hanoi(n, start=1, end=3):
    if n != 0:
        hanoi(n-1, start, 6 - start - end)
        print(f"move piece {n} from {start} to {end}")
        hanoi(n-1, 6 - start - end, end)
        
# 3 1 3
# 2 1 2
# 1 1 3
# move piece 1 from 1 to 3
# move piece 2 from 1 to 2
# 1 3 2
# move piece 1 from 3 to 2
# move piece 3 from 1 to 3
# 2 2 3
# 1 2 1
# move piece 1 from 2 to 1
# move piece 2 from 2 to 3
# 1 1 3
# move piece 1 from 1 to 3

hanoi(3, 1, 3)