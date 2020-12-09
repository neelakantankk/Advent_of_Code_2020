from collections import deque

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

    index = 0
    contiguous = deque()
    while index<len(numbers):
        sum_contiguous = sum(contiguous)
        if sum_contiguous < invalid_number:
            contiguous.append(numbers[index])
            index+=1
        elif sum_contiguous > invalid_number:
            contiguous.popleft()
        elif sum_contiguous == invalid_number:
            break

    print(max(contiguous) + min(contiguous))

if __name__ == '__main__':
    main()
