directions = {(-1,0),(0,-1),(1,0),(0,1)}

matrix = open('input').read().split('\n')
height, width = len(matrix), len(matrix[0])

def search(idx):
    curr_val = int(matrix[idx[0]][idx[1]])
    if curr_val == 9:
        return [idx]
    return [cell for i in adjacent_cells(idx, curr_val) for cell in search(i)]

def adjacent_cells(idx,curr_val):
    return [(idx[0] + dy, idx[1] + dx) for dy, dx in directions
                if 0 <= idx[0] + dy < height and 0 <= idx[1] + dx < width       # boundary check
                and int(matrix[idx[0] + dy][idx[1] + dx]) == curr_val + 1 ]     # slope check

def main(part1):
    sum = 0
    for y in range(height):
        for x in range(width):
            if int(matrix[y][x]) == 0:
                if(part1): sum += len(set(search((y,x))))
                else: sum += len(search((y,x)))
    return sum
print(main(True))
print(main(False))
