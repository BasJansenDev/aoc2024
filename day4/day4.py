directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
cross_line_1 = [(-1, -1), (1, 1)]
cross_line_2 = [(-1, 1), (1, -1)]

word = ['M', 'A', 'S']
mas = [['M', 'S'], ['S', 'M']]

matrix = []
height = 0
width = 0

def main(part1):
    init_matrix()
    sum = 0
    for y in range(height):
        for x in range(width):
            if (part1 and get([y, x]) == 'X'):
                for direction in directions:
                    sum += search_direction([y, x], direction)
            if (not part1 and get([y, x]) == 'A'):
                sum += check_cross([y, x])
    return sum

def search_direction(idx, direction):
    for letter in word:
        idx = increment(idx, direction)
        if (not check_boundaries(idx) or not get(idx) == letter):
            return False
    return True

def check_cross(idx):
    line1 = [get(increment(idx, point)) for point in cross_line_1 if check_boundaries(increment(idx, point))] in mas
    line2 = [get(increment(idx, point)) for point in cross_line_2 if check_boundaries(increment(idx, point))] in mas
    return line1 and line2

def get(idx):
    return matrix[idx[0]][idx[1]]

def increment(idx, dir):
    return [idx[0] + dir[0], idx[1] + dir[1]]

def check_boundaries(idx):
    return idx[0] >= 0 and idx[0] < height and idx[1] >= 0 and idx[1] < width

def init_matrix():
    global matrix
    global height
    global width
    f = open('input')
    matrix = f.read().split('\n')
    height = len(matrix)
    width = len(matrix[0])


print(main(True))
print(main(False))