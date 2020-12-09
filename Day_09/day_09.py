def main():
    with open('input','r') as infile:
        numbers = [int(line.strip()) for line in infile.readlines()]

    preamble_length = 25

    for index,number in enumerate(numbers[preamble_length:],start=25):
        diffs = [x for x in map(lambda y: abs(number - y),numbers[index-preamble_length:index])]
        if set(diffs).intersection(set(numbers[index-preamble_length:index])) == set():
            print(number)
            break

if __name__ == '__main__':
    main()
