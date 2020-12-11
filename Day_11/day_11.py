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
    
def print_layout(layout,label=None):
    if label is not None:
        print("{:-^80}".format(label))
    for row in layout:
        print(''.join(row))

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
        try:
            row_num = current_seat_row + value[0]
            col_num = current_seat_column + value[1]
            if row_num<0:
                row_num = len(seats)
            if col_num<0:
                col_num = len(seats)
            adjacent[key] = seats[row_num][col_num]
        except IndexError:
            adjacent[key] = None

    return adjacent


def main():
    filename = 'example'
    filename = 'input'
    with open(filename,'r') as infile:
        seats = [list(line.strip()) for line in infile.readlines()]

#    print_layout(seats,"Seats at the beginning")


    while True:
        new_layout = []
        for row_index, row in enumerate(seats):
            new_row = []
            for col_index,seat in enumerate(row):
                adjacent = get_adjacent_seats(seats,row_index, col_index)
                #print(f"Seat ({row_index}, {col_index}) --> {adjacent}")
                if seat == '.':
                    new_row.append(seat)
                elif list(adjacent.values()).count("#") >= 4:
                    new_row.append("L")
                elif list(adjacent.values()).count("#") == 0:
                    new_row.append("#")
                else:
                    new_row.append(seat)
            new_layout.append(new_row)

        if are_layouts_equal(seats,new_layout):
            print(count_occupied_seats(seats))
#            print_layout(seats,"Final Seats")
#            print_layout(new_layout,"Final New Layout")
            break
        else:
#            print_layout(new_layout,"New Layout")
            seats = new_layout.copy()
            new_layout = []
            



if __name__ == '__main__':
    main()
