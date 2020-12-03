def main():
    with open('input','r') as infile:
        lines = [line.strip() for line in infile]

    right,down = (0,0)

    trees = 0

    while down<len(lines) - 1:
        right = right+3
        down = down+1

        line = lines[down]

        if right >= len(line):
            right = right - len(line)
        if line[right] == '#':
            trees +=1

    print(trees)


if __name__ == '__main__':
    main()
