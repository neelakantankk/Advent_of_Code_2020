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
    boat_coords = (0,0)
    waypoint_coords = (10,1)
    movements = {
        'N':(0,1),
        'E':(1,0),
        'S':(0,-1),
        'W':(-1,0),
        }

    for instruction,value in instructions:
        if instruction in 'LR':
            # The waypoint is rotated using vector rotation.
            # value is converted to radians. L is counterclockwise, R is clockwise
            # Value is negative if rotation is clockwise, positive otherwise
            # The waypoint coords are then replaced with the rotated vector.

            x1,y1 = waypoint_coords
            if instruction == 'R':
                value_rad = math.radians(value * (-1))
            else:
                value_rad = math.radians(value)
            x2 = int(x1 * math.cos(value_rad)) - int(y1 * math.sin(value_rad))
            y2 = int(x1 * math.sin(value_rad)) + int(y1 * math.cos(value_rad))

            waypoint_coords = (x2,y2)
        elif instruction in 'NSEW':
            i,j = movements[instruction]
            x1,y1 = waypoint_coords
            x2 = i*value
            y2 = j*value
            waypoint_coords = (x1+x2, y1+y2)

        elif instruction == 'F':
            x1,y1 = boat_coords
            x2,y2 = waypoint_coords
            boat_coords = ((x1 + (x2 * value)),(y1 + (y2 * value)))

    # Manhattan distance
    print(abs(boat_coords[0]) + abs(boat_coords[1]))

if __name__ == '__main__':
    main()
