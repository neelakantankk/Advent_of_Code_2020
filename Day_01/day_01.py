#!/usr/bin/env python3
def main():
    input_file = open('input','r')
    nums = [int(line.strip()) for line in input_file.readlines()]

    diff_nums = [x for x in map(lambda x: (2020 - x),nums)]

    filter_nums = [x for x in filter(lambda x: x in nums,diff_nums)]

    print(nums)
    print(diff_nums)
    print(filter_nums)
    print(filter_nums[1]*filter_nums[0])

if __name__ == '__main__':
    main()


