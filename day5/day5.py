from collections import defaultdict

rules = defaultdict(set)

def main(part1):
    updates = read_input()
    result = []
    for update in updates:
        legit = True
        for i in range(len(update)):
            if not set(update[1 + i:]).issubset(rules[update[i]]):
                legit = False
        if part1 and legit:
            result.append(update)
        elif not (part1 or legit):
            result.append(fix_illegal_update(update))
    return sum(lst[len(lst) // 2] for lst in result)

def fix_illegal_update(update):
    illegal = True
    while illegal:
        illegal = False
        for i in range(len(update) - 1):
            if not set(update[1 + i:]).issubset(rules[update[i]]):
                update[i], update[i + 1] = update[i + 1], update[i]
                illegal = True
    return update

def read_input():
    f = open('input')
    a, b = f.read().split('\n\n')
    for line in a.strip().split('\n'):
        key, value = map(int, line.split('|'))
        rules[key].add(value)
    return [list(map(int, line.split(','))) for line in b.strip().split('\n')]

print(main(True))
print(main(False))
