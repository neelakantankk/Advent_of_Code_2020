import re

def apply_mask(mask,value):
    mask_pos = [(index,val) for index,val in enumerate(mask) if val!='X']
    for pos,val in mask_pos:
        value = value[:pos] + val + value[pos+1:]
    return value

def main():
    filename='input'
#    filename='example'

    with open(filename,'r') as infile:
        entries = [(left.strip(),right.strip()) for left,right in [line.strip().split("=") for line in infile.readlines()]]

    mem = dict()

    for entry,value in entries:
        if entry == 'mask':
            mask = value
        else:
            key = re.search(r'mem\[(\d+)\]',entry).group(1)
            val = f"{int(value):036b}"
            mem[key] = int(apply_mask(mask,val),base=2)

    print(sum(mem.values()))

if __name__ == '__main__':
    main()
