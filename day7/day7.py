def calculate(result, expression, parts):
    if parts == []:
        return expression == result
    return calculate(result, expression + parts[0], parts[1:]) \
        or calculate(result, expression * parts[0], parts[1:]) \
        or (not part1 and calculate(result, int(str(expression) + str(parts[0])), parts[1:]))

def main():
    input = open('input').read().split('\n')
    sum = 0
    for equation in input:
        result, parts = int(equation.split(':')[0]), list(map(int, equation.split(':')[1].strip().split()))
        sum += result if calculate(result, parts[0], parts[1:]) else 0
    return sum

part1 = True
print(main())
part1 = False
print(main())
