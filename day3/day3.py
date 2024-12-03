import re

mul_pattern = r"mul\((\d+),(\d+)\)"
do_pattern = r"do\(\)"
dont_pattern = r"don't\(\)"
pattern = f"({mul_pattern})|({do_pattern})|({dont_pattern})"

def main(part1):
    text = read_input()
    sum = 0
    do = True
    for match in re.finditer(pattern, text):
        if match.group(1) and (do or part1):
            sum += int(match.group(2)) * int(match.group(3))
        elif match.group(4):
            do = True
        elif match.group(5):
            do = False
    return sum

def read_input():
    f = open('input')
    return f.read()

print(main(True))
print(main(False))