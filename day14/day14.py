import re
from PIL import Image, ImageDraw

width = 101
height = 103

def main(p1):
    robots = open('input').read().split('\n')
    if p1:
        final = calc(robots,100)
        height_half = height // 2
        width_half = width // 2
        q1, q2, q3, q4 = 0, 0, 0, 0
        for x, y in final:
            if x < width_half:
                if y < height_half:
                    q1 += 1
                elif y > height - height_half:
                    q3 += 1
            elif x > width_half:
                if y < height_half:
                    q2 += 1
                elif y > height_half:
                    q4 += 1
        return q1 * q2 * q3 * q4
    else:
        final = calc(robots, 6668)
        create_image_from_grid(make_grid(final))

def calc(robots,n):
    final = []
    for robot in robots:
        numbers = list(map(int, re.findall(r'-?\d+', robot)))
        px,py,vx,vy = numbers
        final.append(((px+n*vx) % width,(py+n*vy) % height))
    return final


def make_grid(coordinates):
    grid = [['.' for _ in range(height)] for _ in range(width)]
    for x, y in coordinates:
        if 0 <= x < width and 0 <= y < height:
            grid[x][y] = 'X'
    return grid

def create_image_from_grid(grid, cell_size=10):
    image_size = (height * cell_size, width * cell_size)

    img = Image.new('RGB', image_size, color='white')
    draw = ImageDraw.Draw(img)
    for row_idx, row in enumerate(grid):
        for col_idx, cell in enumerate(row):
            if cell != '.':
                draw.rectangle([(col_idx * cell_size, row_idx * cell_size),
                                ((col_idx + 1) * cell_size,
                                 (row_idx + 1) * cell_size)], fill='black')
    img.save('picture.png')

print(main(True))
main(False)
