import math

def main():
    #filename = 'example.txt'
    filename = 'input'
    with open(filename,'r') as infile:
        instructions = [(line[0],int(line.strip()[1:]))
                        for line in infile.readlines()]

    # Model position on a grid, with N and S being +y and -y
    # and E and W being +x and -x

    coords = [0,0]
    # Direction is being modelled as a tuple where the
    # first number says whether to change the x or y coord
    # and the second number says whether to increase or
    # decrease the coord
    movements = {
        'N':(0,1),
        'E':(1,1),
        'S':(0,-1),
        'W':(1,-1),
        'F':(1,1)}

    for instruction,value in instructions:
        if instruction in 'NSWEF':
            axis,direction = movements[instruction]
            coords[axis] += int((direction * value))
        elif instruction in 'LR':
            # Turns change the value of 'F', changing the sign of the coord
            # according to the value of turn and the direction of turn
            # 180 degrees flips the sign
            # 90 and 270 degrees change it depending on the current sign and
            # whether or not the turn is R or L
            # the factors are all hand-calculated

            forwards = movements['F']
            turn_factor = {'L':0,'R':1}
            if value == 180:
                movements['F'] = (forwards[0], int(forwards[1]*(-1)))
            elif value == 90:
                direction = 1 - forwards[0]
                turn = int(forwards[1] * math.pow(
                    -1,1 + forwards[0] - turn_factor[instruction]))
                movements['F'] = (direction,turn)
            elif value == 270:
                direction = 1 - forwards[0]
                turn = int(forwards[1] * math.pow(
                    -1,2 + forwards[0] - turn_factor[instruction]))
                movements['F'] = (direction,turn)

    print(abs(coords[0]) + abs(coords[1]))

if __name__ == '__main__':
    main()