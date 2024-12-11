from functools import lru_cache

@lru_cache(maxsize=None)

def step(n, depth, stone):
    if n == depth:
        return 1
    elif int(stone) == 0:
        return step(n,depth+1,'1')
    elif len(stone) % 2 == 0:
        mid = len(stone) // 2
        return step(n, depth+1, stone[:mid]) + step(n, depth+1, str(int(stone[mid:])))
    else:
        return step(n, depth+1, str(int(stone)*2024))

def main(part1):
    stones = open('input').read().split(' ')
    if(part1):
        n = 25
    else:
        n = 75
    sum = 0
    for stone in stones:
        sum += step(n,0,stone)
    return sum

print(main(True))
print(main(False))
