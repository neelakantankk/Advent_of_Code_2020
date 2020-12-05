def parse_b_pass(b_pass):
    lower_row,higher_row = (0,127)
    lower_column,higher_column = (0,7)

    for ch in b_pass[0:6]:
        if ch=='F':
            higher_row = (lower_row + higher_row) // 2
        elif ch=='B':
            lower_row = ((lower_row + higher_row) //2) + 1

    for ch in b_pass[-3:-1]:
        if ch=='L':
            higher_column = (lower_column + higher_column) // 2
        elif ch=='R':
            lower_column = ((lower_column + higher_column) // 2) + 1

    if b_pass[6] == 'F':
        row = lower_row
    elif b_pass[6] == 'B':
        row = higher_row

    if b_pass[-1] == 'L':
        column = lower_column
    elif b_pass[-1] == 'R':
        column = higher_column

    return ((row * 8) + column)

def main():

    with open("input","r") as infile:
        b_passes = [line.strip() for line in infile.readlines()]

    max_id = 0
    seat_ids = []

    for b_pass in b_passes:
        seat_id = parse_b_pass(b_pass)

        if seat_id > max_id:
            max_id = seat_id

        seat_ids.append(seat_id)

    print(max_id)
    seat_ids_sorted = sorted(seat_ids)

    missing = {x for x in range(seat_ids_sorted[0],seat_ids_sorted[-1]+1)} - set(seat_ids_sorted)

    print(missing.pop())


if __name__ == '__main__':
    main()


