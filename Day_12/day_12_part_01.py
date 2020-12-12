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
    coords = [0,0]
    movements = {
        'N':(1,0),
        'E':(0,1),
        'S':(-1,0),
        'W':(0,-1),
        'F':(0,1)}

    for instruction,value in instructions:
        if instruction in 'LR':
            # 'F' is rotated using vector rotation.
            # value is converted to radians. L is counterclockwise, R is clockwise
            # Value is negative if rotation is counterclockwise, positive otherwise
            # 'F' is then replaced with the rotated vector.

            x1,y1 = movements['F']
            if instruction == 'L':
                value_rad = math.radians(value * (-1))
            else:
                value_rad = math.radians(value)
            x2 = int((x1 * math.cos(value_rad)) - (y1 * math.sin(value_rad)))
            y2 = int((x1 * math.sin(value_rad)) + (y1 * math.cos(value_rad)))
            movements['F'] = (x2,y2)
        else:
            x,y = movements[instruction]
            x1 = x*value
            y1 = y*value
            coords[0] += x1
            coords[1] += y1

    # Manhattan distance
    print(abs(coords[0]) + abs(coords[1]))

if __name__ == '__main__':
    main()
