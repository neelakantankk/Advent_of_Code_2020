def main():
    with open('input.txt','r') as infile:
        jolts = [int(line.strip()) for line in infile.readlines()]

    jolts_sorted = sorted(jolts)

    diffs = {1:0, 2:0, 3:0}

    for index,jolt in enumerate(jolts_sorted[:-1]):
        diff = jolts_sorted[index+1] - jolt
        diffs[diff]+=1

    diffs[3]+=1
    diffs[1]+=1

    print(diffs[1] * diffs[3])
    print(jolts_sorted)

if __name__ == '__main__':
    main()

