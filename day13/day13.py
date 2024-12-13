from sympy import symbols, Eq, solve
import re

def calc(x1, x2, y1, y2, c1, c2):
    a, b = symbols('a b', integer=True)
    solutions = solve((Eq(a * x1 + b * y1, c1), Eq(a * x2 + b * y2, c2)), (a, b))
    if solutions:
        a_val, b_val = solutions[a], solutions[b]
        if a_val > 0 and b_val > 0 and a_val.is_integer and b_val.is_integer:
            return 3 * int(a_val) + int(b_val)
    return 0

def main2(part1):
    value = 0
    machines = open('input').read().split('\n\n')
    for machine in machines:
        numbers = list(map(int, re.findall(r'[+=]?(\d+)', machine)))
        bA_x, bA_y, bB_x, bB_y, prize_x, prize_y = numbers
        if (not part1):
            prize_x += 10000000000000
            prize_y += 10000000000000
        value += calc(bA_x, bA_y, bB_x, bB_y, prize_x, prize_y)
    return value

print(main2(True))
print(main2(False))