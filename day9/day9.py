def main(part1):
    line = open('input').read()
    if part1:
        line = translate1(line)
        part1swap(line)
    else:
        files,spaces = translate2(line)
        line = part2swap(files,spaces)
    return sum(i * int(line[i]) for i in range(len(line)) if line[i] != '.')


def part1swap(line):
    i, j = 0, len(line) - 1
    while i < j:
        if line[j] == '.':
            j -= 1
        elif line[i] == '.':
            line[i], line[j] = line[j], line[i]
        i += (line[i] != '.')

def part2swap(files, spaces):
    new_files = []
    for file in reversed(files):
        inserted = False
        for i, space in enumerate(spaces):
            if space[0] >= file[0]:
                break
            if space[1] >= len(file[1]):
                new_files.insert(0, (space[0], file[1]))
                spaces[i] = (space[0] + len(file[1]), space[1] - len(file[1]))
                inserted = True
                break
        if not inserted:
            new_files.insert(0, (file[0], file[1]))
    new_files.sort()
    return get_string(new_files)

def get_string(tuples):
    max_position = max(t[0] for t in tuples)
    result = ['.'] * (max_position + 1)
    for position, text_list in tuples:
        result[position:position+len(text_list)] = text_list
    return result


def translate1(line):
    newline = []
    for i in range(len(line)):
        if i % 2 == 0:
            newline += (int(line[i])*[str(i//2)])
        else:
            newline += str(int(line[i])*'.')
    return newline

def translate2(line):
    files = []
    spaces = []
    pos = 0
    i = 0
    for i in range(len(line)):
        if i % 2 == 0:
            files.append((pos,int(line[i])*[str(i//2)]))
        else:
            if int(line[i]) != 0:
                spaces.append((pos,int(line[i])))
        pos += int(line[i])
    return files, spaces
print(main(True))
print(main(False))
