def main(part1):
    input = [[int(x) for x in i.split(' ')] for i in open('input').read().split('\n')]
    if(part1):
        return sum(check(lst) for lst in input)
    return sum(1 for lst in input if any(check(lst[:i] + lst[i + 1:]) for i in range(len(lst))))


def check(sublist):
    ascending = all(earlier > later for earlier, later in zip(sublist, sublist[1:]))
    descending = all(earlier < later for earlier, later in zip(sublist, sublist[1:]))
    diff = all(abs(earlier - later) <= 3 for earlier, later in zip(sublist, sublist[1:]))
    return (ascending or descending) and diff

print(main(True))
print(main(False))
