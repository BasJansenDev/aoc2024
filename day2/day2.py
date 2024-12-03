def main(part1):
    input = input_as_list()
    sum = 0
    for lst in input:
        if (part1):
            sum += check(lst)
        else:
            for i in range(len(lst)):
                sublist = lst[:i] + lst[i + 1:]
                if (check(sublist)):
                    sum += 1
                    break
    return sum

def check(sublist):
    ascending = all(earlier > later for earlier, later in zip(sublist, sublist[1:]))
    descending = all(earlier < later for earlier, later in zip(sublist, sublist[1:]))
    diff = all(abs(earlier - later) <= 3 for earlier, later in zip(sublist, sublist[1:]))
    return (ascending or descending) and diff

def input_as_list():
    f = open('input')
    a = f.read().split('\n')
    b = []
    for i in a:
        c = i.split(' ')
        for d in range(len(c)):
            c[d] = int(c[d])
        b.append(c)
    return b

print(main(True))
print(main(False))
