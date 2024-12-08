def main(part1):
    first,second = map(list, zip(*[i.split('   ') for i in open('input').read().split('\n')]))
    first.sort()
    second.sort()
    sum = 0
    for i in range(len(first)) :
        if(part1): sum += abs(int(first[i]) - int(second[i]))
        else:      sum += int(second.count(first[i]))*int(first[i])
    return sum

print(main(True))
print(main(False))
