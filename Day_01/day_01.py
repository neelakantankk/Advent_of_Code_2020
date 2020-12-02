#!/usr/bin/env python3
from functools import reduce
def main():
    input_file = open('input','r')
    nums = [int(line.strip()) for line in input_file.readlines()]
    ans = set()

    for x in map(lambda x: (2020 - x),nums):
        for y in map(lambda y:x - y, nums):
            if y in nums:
                ans.add(y)

    print(ans)
    print(reduce(lambda x,y: x*y,ans,1))

if __name__ == '__main__':
    main()


