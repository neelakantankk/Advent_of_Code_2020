def main():
    with open('input','r') as infile:
        entries = [line.replace('\n','').strip() for line in infile.read().split("\n\n")]

    sum_counts = 0

    for entry in entries:
        sum_counts += len(set(entry))

    print(sum_counts)


if __name__ == '__main__':
    main()
