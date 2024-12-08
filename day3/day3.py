import re

mul_pattern = r"mul\((\d+),(\d+)\)"
do_pattern = r"do\(\)"
dont_pattern = r"don't\(\)"
pattern = f"({mul_pattern})|({do_pattern})|({dont_pattern})"

def main(part1):
    sum = 0
    do = True
    for match in re.finditer(pattern, open('input').read()):
        if match.group(1) and (do or part1):
            sum += int(match.group(2)) * int(match.group(3))
        elif match.group(4):
            do = True
        elif match.group(5):
            do = False
    return sum
    
print(main(True))
print(main(False))
