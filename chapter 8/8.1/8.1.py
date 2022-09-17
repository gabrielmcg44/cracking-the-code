
ways = {}

def staircase_ways_up(n):
    if n < 0:
        return 0
    if n == 0: # erro: n in [0, 1], também funciona, mas n == 0 era suficiente
        return 1
        
    if n not in ways.keys():  # erro: coloquei .Keys
        ways[n] = staircase_ways_up(n-1) + staircase_ways_up(n-2) + staircase_ways_up(n-3)
        
    return ways[n]
    
print(staircase_ways_up(1))
print(staircase_ways_up(2))
print(staircase_ways_up(3))
print(staircase_ways_up(4))
print(staircase_ways_up(5))
