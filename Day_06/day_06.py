from functools import reduce
def main():
    with open('input','r') as infile:
        entries = [[set(x) for x in line.strip().split("\n")] for line in infile.read().split("\n\n")]

    sum_counts = 0

    for entry in entries:
        sum_counts += len(reduce(lambda x,y: x & y,entry))

    print(sum_counts)


if __name__ == '__main__':
    main()
