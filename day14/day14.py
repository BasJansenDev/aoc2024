import re
from PIL import Image, ImageDraw, ImageFont
import os

width = 101
height = 103

def main():
    robots = open('input').read().split('\n')
    for n in range(10):
        final = []
        for robot in robots:
            numbers = list(map(int, re.findall(r'-?\d+', robot)))
            px,py,vx,vy = numbers
            final.append(((px+n*vx) % width,(py+n*vy) % height))
        create_image_from_grid(make_grid(final),n)



    height_half = height // 2
    width_half = width // 2
    q1,q2,q3,q4 = 0,0,0,0
    for x,y in final:
        if x < width_half:
            if y < height_half:
                q1 += 1
            elif y > height-height_half:
                q3 += 1
        elif x > width_half:
            if y < height_half:
                q2 +=1
            elif y > height_half:
                q4 += 1
    return q1*q2*q3*q4

def make_grid(coordinates):
    grid = [['.' for _ in range(height)] for _ in range(width)]
    for x, y in coordinates:
        if 0 <= x < width and 0 <= y < height:  # Ensure coordinates are within bounds
            grid[x][y] = 'X'  # You can replace '1' with any other logic if needed
    return grid

def create_image_from_grid(grid,n, cell_size=10):
    image_size = (height * cell_size, width * cell_size)

    img = Image.new('RGB', image_size, color='white')
    draw = ImageDraw.Draw(img)
  
    for row_idx, row in enumerate(grid):
        for col_idx, cell in enumerate(row):
            if cell != '.':
                draw.rectangle([top_left, bottom_right], fill='black')

    img.save('pictures/picture' + str(n) + '.png')
print(main())
