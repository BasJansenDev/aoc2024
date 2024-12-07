from itertools import product

def main(part1):
    input = read_input()
    success = 0
    for equation in input:
        result, parts = equation.split(':')
        result = int(result)
        parts = list(map(int,parts.strip().split(' ')))
        operators = []
        if(part1):
            operators = list(product(['+', '*'], repeat=len(parts)-1))
        else:
            operators = list(product(['+', '*', '||'], repeat=len(parts)-1))
        for ops in operators:
            expression = parts[0]
            for i, op in enumerate(ops):
                if op == '+':
                    expression += parts[i + 1]
                elif op == '*':
                    expression *= parts[i + 1]
                else:
                    expression = int(str(expression) + str(parts[i+1]))
            if(expression == result):
                success += result
                break
    return success


def read_input():
    f = open('input')
    return f.read().split('\n')

print(main(True))
print(main(False))
