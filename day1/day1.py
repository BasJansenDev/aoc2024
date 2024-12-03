example = "3   4.4   3.2   5.1   3.3   9.3   3"

def main(part1):
    first,second = split_list(input_as_list())
    first.sort()
    second.sort()
    sum = 0
    for i in range(len(first)) :
        if(part1):
            sum += abs(int(first[i]) - int(second[i]))
        else:
            sum += int(second.count(first[i]))*int(first[i])
    return sum


def split_list(list):
    a = []
    b = []
    for i in list:
        c,d = i.split('   ')
        a += [c]
        b += [d]
    return a,b

def input_as_list():
    f = open('input')
    return list(f.read().split('\n'))
    # f = example
    # return list(f.split('.'))

print(main(True))
print(main(False))