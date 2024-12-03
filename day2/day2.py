def main(part1):
    input = input_as_list()
    total = 0
    if(part1):
        total = sum(check(lst) for lst in input)
    else:
        for lst in input:
            for i in range(len(lst)):
                sublist = lst[:i] + lst[i + 1:]
                if (check(sublist)):
                    total += 1
                    break
    return total

def check(sublist):
    ascending = all(earlier > later for earlier, later in zip(sublist, sublist[1:]))
    descending = all(earlier < later for earlier, later in zip(sublist, sublist[1:]))
    diff = all(abs(earlier - later) <= 3 for earlier, later in zip(sublist, sublist[1:]))
    return (ascending or descending) and diff

def input_as_list():
    f = open('input')
    return [[int(x) for x in i.split(' ')] for i in f.read().split('\n')]

print(main(True))
print(main(False))
