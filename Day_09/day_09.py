def main():
    with open('input','r') as infile:
        numbers = [int(line.strip()) for line in infile.readlines()]

    preamble_length = 25
    invalid_number = None

    for index,number in enumerate(numbers[preamble_length:],start=25):
        diffs = [x for x in map(lambda y: abs(number - y),numbers[index-preamble_length:index])]
        if set(diffs).intersection(set(numbers[index-preamble_length:index])) == set():
            invalid_number = number
            break

    print(invalid_number)

    for index in range(0,len(numbers)):
        number_of_entries = 1
        flag = False
        while sum(numbers[index:number_of_entries+index]) < invalid_number:
            number_of_entries += 1
            if sum(numbers[index:number_of_entries+index]) == invalid_number:
                print(max(numbers[index:number_of_entries + index]) +
                        min(numbers[index:number_of_entries + index]))
                flag = True
                break
        if flag == True:
            break

if __name__ == '__main__':
    main()
