import re
from itertools import product

def apply_mask(mask,value):
    mask_pos = [(index,val) for index,val in enumerate(mask) if val=='1']
    for pos,val in mask_pos:
        value = value[:pos] + val + value[pos+1:]
    x_pos = [index for index,val in enumerate(mask) if val=='X']
    combinations = [x for x in product('01',repeat=len(x_pos))]
    mems = []
    for combination in combinations:
        for pos,val in zip(x_pos,combination):
            value = value[:pos] + val + value[pos+1:]
        mems.append(value)
    return mems

def main():
    filename='input'
    #filename='example2'

    with open(filename,'r') as infile:
        entries = [(left.strip(),right.strip()) for left,right in [line.strip().split("=") for line in infile.readlines()]]

    memory = dict()

    for entry,value in entries:
        if entry == 'mask':
            mask = value
        else:
            key = re.search(r'mem\[(\d+)\]',entry).group(1)
            val = f"{int(key):036b}"
            mems_to_change = apply_mask(mask,val)
            for mem in mems_to_change:
                memory[mem] = int(value)

    print(sum(memory.values()))

if __name__ == '__main__':
    main()
