def main(part1):
    line = open('testinput').read()
    files,spaces = translate(line, part1)
    line = swap(files,spaces)
    return sum(i * int(line[i]) for i in range(len(line)) if line[i] != '.')

def swap(files, spaces):
    new_files = []
    for file in reversed(files):
        for i, space in enumerate(spaces):
            if space[0] >= file[0]:
                new_files.insert(0, (file[0], file[1]))
                break
            if space[1] >= len(file[1]):
                new_files.insert(0, (space[0], file[1]))
                spaces[i] = (space[0] + len(file[1]), space[1] - len(file[1]))
                break
    new_files.sort()
    return get_string(new_files)

def get_string(tuples):
    max_position = max(t[0] for t in tuples)
    result = ['.'] * (max_position + 1)
    for position, text_list in tuples:
        result[position:position+len(text_list)] = text_list
    return result

def translate(line, part1):
    files = []
    spaces = []
    pos, i = 0, 0
    for i in range(len(line)):
        if i % 2 == 0:
            if part1:
                for j in range(int(line[i])):
                    files.append((pos+j,[str(i//2)]))
            else:
                files.append((pos,int(line[i])*[str(i//2)]))
        else:
            spaces.append((pos,int(line[i])))
        pos += int(line[i])
    return files, spaces
print(main(True))
print(main(False))
