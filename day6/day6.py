import copy

directions = {0:(-1,0),1:(0,1),2:(1,0),3:(0,-1)}
mapping = ['^','>','v','<']
precomputed_neighbors = {}

layout = []
dupes = 0
height = 0
width = 0
original_direction = 0
curr_direction = 0

def main(part1):
    read_input()
    precompute_neighbors()
    pos = find_guard()
    reached = full_run(pos, False)
    if part1:
        return len(reached)

    obstacles = get_obstacles(reached)
    original_map = copy.deepcopy(layout)
    for obstacle in obstacles:
        layout[obstacle[0]][obstacle[1]] = 'O'
        full_run(pos, True)
        layout[obstacle[0]][obstacle[1]] = original_map[obstacle[0]][obstacle[1]]
    return dupes

def get_obstacles(reached):
    obstacles = set()
    for position in reached:
        for d in directions:
            inc = precomputed_neighbors[position][d]
            if inc != None:
                obstacles.add(tuple(inc))
    return obstacles

def full_run(pos, dupecheck):
    global dupes
    curr_direction = original_direction
    reached = {tuple(pos)}
    dupe = None

    while True:
        next_pos = precomputed_neighbors[pos][curr_direction]
        if next_pos == None:
            return reached
        if check_wall(pos, curr_direction):
            curr_direction = (curr_direction + 1) % 4
            continue
        pos = next_pos
        if pos not in reached:
            reached.add(pos)
            dupe = None
        elif dupecheck:
            if dupe is None:
                dupe = pos
            elif dupe == pos:
                dupes += 1
                return

def find_guard():
    return next((tuple([y, x]) for y in range(height) for x in range(width) if layout[y][x] in mapping), None)


def check_wall(idx, direction):
    pos = precomputed_neighbors[idx][direction]
    return layout[pos[0]][pos[1]] == '#' or layout[pos[0]][pos[1]] == 'O'

def precompute_neighbors():
    global precomputed_neighbors
    precomputed = {}
    for y in range(height):
        for x in range(width):
            neighbors = []
            for d in directions.values():
                ny, nx = y + d[0], x + d[1]
                if check_boundaries([ny,nx]):
                    neighbors.append((ny, nx))
                else:
                    neighbors.append(None)
            precomputed[(y, x)] = neighbors
    precomputed_neighbors = precomputed

def check_boundaries(idx):
    return 0 <= idx[0] < height and 0 <= idx[1] < width

def read_input():
    global layout, width, height
    f = open('input')
    layout = list(map(list,f.read().split('\n')))
    height = len(layout)
    width = len(layout[0])

print(main(True))
print(main(False))
