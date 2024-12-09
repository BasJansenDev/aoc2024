def main(part1):
    line = open('testinput').read()
    files,spaces = translate(line, part1)
    line = swap(files,spaces)
    return sum(
        (index+i) * int(val)
        for index, text_list in line
        for i, val in enumerate(text_list)
        if val != '.'
    )

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
    return new_files

def translate(line, part1):
    files, spaces = [],[]
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
