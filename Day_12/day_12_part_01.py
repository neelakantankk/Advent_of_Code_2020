import math

def main():
    #filename = 'example'
    filename = 'input'
    with open(filename,'r') as infile:
        instructions = [(line[0],int(line.strip()[1:]))
                        for line in infile.readlines()]


    # Boat position is modelled as a vector. The movement commands are
    # modelled as unit vectors. Rotation commands affect only the unit
    # vector 'F'. Coordinates are changed using vector addition.
    coords = (0,0)
    movements = {
        'N':(0,1),
        'E':(1,0),
        'S':(0,-1),
        'W':(-1,0),
        'F':(1,0)}

    for instruction,value in instructions:
        if instruction in 'LR':
            # 'F' is rotated using vector rotation.
            # value is converted to radians. L is counterclockwise, R is clockwise
            # Value is negative if rotation is clockwise, positive otherwise
            # 'F' is then replaced with the rotated vector.

            i,j = movements['F']
            if instruction == 'R':
                value_rad = math.radians(value * (-1))
            else:
                value_rad = math.radians(value)
            x2 = int((i * math.cos(value_rad)) - (j * math.sin(value_rad)))
            y2 = int((i * math.sin(value_rad)) + (j * math.cos(value_rad)))
            movements['F'] = (x2,y2)
        else:
            i,j = movements[instruction]
            x1,y1 = coords
            x2 = i*value
            y2 = j*value

            coords = (x1 + x2, y1 + y2)

    # Manhattan distance
    print(abs(coords[0]) + abs(coords[1]))

if __name__ == '__main__':
    main()
