import time

def are_layouts_equal(old_layout, new_layout):
    for old_row,new_row in zip(old_layout,new_layout):
        for old_seat,new_seat in zip(old_row,new_row):
            if old_seat != new_seat:
                return False
    return True

def count_occupied_seats(seats):
    count = 0
    for row in seats:
        count+= len([x for x in row if x == '#'])
    return count
    
def get_adjacent_seats(seats,current_seat_row, current_seat_column):
    adjacent = dict()
    directions = {
            'up':(-1,0),
            'down':(1,0),
            'left':(0,-1),
            'right':(0,1),
            'd_u_l':(-1,-1),
            'd_u_r':(-1,1),
            'd_d_l':(1,-1),
            'd_d_r':(1,1)
            }
    for key,value in directions.items():
        if current_seat_row == 0 and (key in ['up','d_u_l','d_u_r']):
            adjacent[key] = '.'
        elif current_seat_row == len(seats) - 1 and (key in ['down','d_d_r','d_d_l']):
            adjacent[key] = '.'
        elif current_seat_column == 0 and (key in ['left','d_u_l','d_d_l']):
            adjacent[key] = '.'
        elif current_seat_column == len(seats[0]) - 1 and (key in ['right','d_d_r','d_u_r']):
            adjacent[key] = '.'
        else:
            row_num = current_seat_row + value[0]
            col_num = current_seat_column + value[1]
            adjacent[key] = seats[row_num][col_num]
    return adjacent

def main():
    filename = 'example'
    filename = 'input'
    with open(filename,'r') as infile:
        seats = [list(line.strip()) for line in infile.readlines()]

    START = time.perf_counter_ns()
    while True:
        new_layout = []
        for row_index, row in enumerate(seats):
            new_row = []
            for col_index,seat in enumerate(row):
                if seat == '.':
                    new_row.append(seat)
                else:
                    adjacent = get_adjacent_seats(seats,row_index, col_index)
                    if list(adjacent.values()).count("#") >= 4:
                        new_row.append("L")
                    elif list(adjacent.values()).count("#") == 0:
                        new_row.append("#")
                    else:
                        new_row.append(seat)

            new_layout.append(new_row)

        if are_layouts_equal(seats,new_layout):
            print(count_occupied_seats(seats))
            break
        else:
            seats = new_layout.copy()
            new_layout = []

    END = time.perf_counter_ns()
    print(f"Part 1 took {END - START} nanoseconds")

if __name__ == '__main__':
    main()
