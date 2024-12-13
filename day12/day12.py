directions = [(-1,0),(0,-1),(1,0),(0,1)]

matrix = open('input').read().split('\n')
height, width = len(matrix), len(matrix[0])
def main():
    total = 0
    seen = set()
    for y in range(height):
        for x in range(width):
            if (y,x) in seen:
                continue
            letter = matrix[y][x]
            region, perim = find_regions(set(), (y,x), letter)
            if(part1):
                total += len(region) * perim
            else:
                total += len(region) * calc_sides(region)
            seen |= region
    return total

def calc_sides(region):
    sides = 0
    active = {'top': False, 'right': False, 'bottom' : False, 'left': False}
    for y in range(height):
        for x in range(width):
            if (y,x) in region:
                if(not boundary_check((y,x),-1,0) or not (y-1,x) in region):
                    if(active['top'] == False):
                        sides += 1
                        active['top'] = True
                else:
                    active['top'] = False
                if(not boundary_check((y,x),1,0) or not (y+1,x) in region):
                    if (active['bottom'] == False):
                        sides += 1
                        active['bottom'] = True
                else:
                    active['bottom'] = False
            else:
                active['top'], active['bottom'] = False, False
    for x in range(width):
        for y in range(height):
            if (y,x) in region:
                if(not boundary_check((y,x),0,-1) or not (y,x-1) in region):
                    if(active['left'] == False):
                        sides += 1
                        active['left'] = True
                else:
                    active['left'] = False
                if(not boundary_check((y,x),0,1) or not (y,x+1) in region):
                    if (active['right'] == False):
                        sides += 1
                        active['right'] = True
                else:
                    active['right'] = False
            else:
                active['left'], active['right'] = False, False
    return sides

def find_regions(region,idx, letter):
    if idx in region:
        return region, 0
    region.add(idx)
    adj = adjacent_cells(idx,letter)
    if adj.issubset(region):
            return region,4-len(adj)
    else:
        diff = adj-region
        sub_perim = 0
        for d in diff:
            r, p = find_regions(region, d, letter)
            region |= r
            sub_perim += p
        return region, sub_perim + (4-len(adj))

def adjacent_cells(idx,curr_letter):
    return set([(idx[0] + dy, idx[1] + dx) for dy, dx in directions
                if boundary_check(idx,dy,dx)
                and matrix[idx[0] + dy][idx[1] + dx] == curr_letter])

def boundary_check(idx, dy, dx):
    return 0 <= idx[0] + dy < height and 0 <= idx[1] + dx < width

part1 = True
print(main())
part1 = False
print(main())