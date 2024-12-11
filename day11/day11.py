from functools import lru_cache
@lru_cache(maxsize=None)

def step(n, depth, stone):
    if n == depth:
        return 1
    elif int(stone) == 0:
        return step(n,depth+1,'1')
    elif len(stone) % 2 == 0:
        return step(n, depth+1, stone[:len(stone) // 2]) + step(n, depth+1, str(int(stone[len(stone) // 2:])))
    else:
        return step(n, depth+1, str(int(stone)*2024))

def main(part1):
    stones = open('input').read().split()
    n = 25 if part1 else 75
    return sum(step(n, 0, stone) for stone in stones)

print(main(True))
print(main(False))
