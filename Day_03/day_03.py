def get_trees(slope,lines):
    right,down = (0,0)
    right_add, down_add = slope

    trees = 0

    while down<len(lines) - down_add:
        right = right+right_add
        down = down+down_add

        line = lines[down]

        if right >= len(line):
            right = right - len(line)
        if line[right] == '#':
            trees +=1

    return trees


def main():
    with open('input','r') as infile:
        lines = [line.strip() for line in infile]

    slopes = [(1,1),(3,1),(5,1),(7,1),(1,2)]

    trees = 1

    for slope in slopes:
        trees*=get_trees(slope,lines)


    print(trees)


if __name__ == '__main__':
    main()
