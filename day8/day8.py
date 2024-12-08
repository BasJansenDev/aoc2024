from collections import defaultdict

matrix = []
height = 0
width = 0
antinodes = set()

def main(part1):
    read_input()
    antennae = defaultdict(list)
    [antennae[v].append((y, x)) for y in range(height) for x in range(width) if (v := matrix[y][x]) != '.']
    for antenna in antennae.values():
        for i, a in enumerate(antenna):
            for b in antenna[i+1:]:
                if(part1): calculate_points_1(a,b)
                else: calculate_points_2(a, b)
    return len(antinodes)

def calculate_points_1(a,b):
    p1 = 2*b[0] - a[0], 2*b[1]-a[1]
    p2 = 2*a[0] - b[0], 2*a[1]-b[1]
    if check_boundaries(p1): antinodes.add(p1)
    if check_boundaries(p2): antinodes.add(p2)

def calculate_points_2(a, b):
    harmonic = 0
    while True:
        vector = b[0] - a[0], b[1] - a[1]
        p1 = b[0] + harmonic * vector[0], b[1] + harmonic * vector[1]
        p2 = a[0] - harmonic * vector[0], a[1] - harmonic * vector[1]
        if not (check_boundaries(p1) or check_boundaries(p2)): break
        if check_boundaries(p1): antinodes.add(p1)
        if check_boundaries(p2): antinodes.add(p2)
        harmonic += 1

def check_boundaries(idx):
    return 0 <= idx[0] < height and 0 <= idx[1] < width

def read_input():
    global matrix, height, width
    matrix = open('input').read().split('\n')
    height = len(matrix)
    width = len(matrix[0])

print(main(True))
print(main(False))
