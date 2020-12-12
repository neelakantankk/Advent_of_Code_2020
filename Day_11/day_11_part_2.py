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
    
def get_seats(seats, direction, current_seat_row, current_seat_column):
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
    if (((current_seat_row == 0) and (direction in ['up','d_u_l','d_u_r']))
            or ((current_seat_row == len(seats) - 1) and (
                direction in ['down','d_d_l','d_d_r']))
            or ((current_seat_column == 0) and (direction in ['left','d_u_l','d_d_l']))
            or ((current_seat_column == len(seats[0])-1) and (
                direction in ['right','d_u_r','d_d_r']))):
                return '.'
    else:
        row_dir,col_dir = directions[direction]
        if seats[current_seat_row + row_dir][current_seat_column + col_dir] != '.':
            return seats[current_seat_row + row_dir][current_seat_column + col_dir]
        else:
            return get_seats(seats, direction, current_seat_row + row_dir, current_seat_column + col_dir)

def get_all_seats_visible(seats,current_seat_row,current_seat_column):
    adjacent = dict()
    directions = ['up','down','left','right','d_u_l','d_u_r','d_d_l','d_d_r']
    for direction in directions:
        adjacent[direction] = get_seats(seats,direction,current_seat_row,current_seat_column)
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
                    adjacent = get_all_seats_visible(seats,row_index, col_index)
                    if list(adjacent.values()).count("#") >= 5:
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
            seats = new_layout
            new_layout = []
    END = time.perf_counter_ns()
    print(f"Time: {END - START} nanoseconds")

if __name__ == '__main__':
    main()
