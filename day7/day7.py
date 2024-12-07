def calculate(result, expression, parts):
    if parts == []:
        return expression == result
    else:
        return calculate(result, expression + parts[0], parts[1:]) \
            or calculate(result, expression * parts[0], parts[1:]) \
            or (part2 and calculate(result, int(str(expression) + str(parts[0])), parts[1:]))

def main():
    input = read_input()
    success = 0
    for equation in input:
        result, parts = equation.split(':')
        result = int(result)
        parts = list(map(int,parts.strip().split(' ')))
        if(calculate(result, parts[0], parts[1:])):
            success += result
    return success

def read_input():
    f = open('input')
    return f.read().split('\n')

part2 = False
print(main())
part2 = True
print(main())
