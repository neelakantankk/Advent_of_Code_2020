import re
import sys
import time

def main():

    filename = 'example'
    filename = 'input'
    #filename = 'example2'
    START = time.perf_counter_ns()
    with open(filename,'r') as infile:
        notes = [line.strip() for line in infile.read().split("\n\n")]

    fields = {}
    valid_values = set()

    for field_notes in notes[0].split("\n"):
        mo = re.compile(r'^(?P<field>.*?): (\d+)-(\d+) or (\d+)-(\d+)')
        result = mo.search(field_notes)
        low1 = int(result.group(2))
        high1 = int(result.group(3))
        low2 = int(result.group(4))
        high2 = int(result.group(5))
        fields[result.group('field')] = {i for i in range(low1,high1+1)}
        fields[result.group('field')].update(i for i in range(low2,high2+1))
        valid_values.update(fields[result.group('field')])

    pos_fields = {f"pos_{i+1}":set(fields.keys()) for i in range(0,len(fields.keys()))}
    pos_values = {}

    for field_notes in notes[2].split("\n")[1:]:
        nums = [int(i) for i in field_notes.split(",")]
        if not set(nums).difference(valid_values):
            for index,num in enumerate(nums,start=1):
                pos = f"pos_{index}"
                pos_values.setdefault(pos,set()).add(num)

    field_assign = {}

    while len(field_assign.keys()) != len(pos_fields.keys()):
        for pos,values in pos_values.items():
            val_fields = pos_fields[pos]
            invalid = set()
            for field in val_fields:
                if field in field_assign.keys():
                    invalid.add(field)
                else:
                    valid_vals = fields[field]
                    diffs = values - valid_vals
                    if diffs != set():
                        invalid.add(field)
            pos_fields[pos].difference_update(invalid)
            if len(pos_fields[pos]) == 1:
                field = pos_fields[pos].pop()
                field_assign[field] = pos

    my_ticket = [int(i) for i in notes[1].split("\n")[1].split(",")]

    result = 1

    for field,pos in field_assign.items():
        if 'departure' in field:
            index = int(re.search(r'pos_(\d+)',pos).group(1)) - 1
            result*= my_ticket[index]
            
    print(result)
    END = time.perf_counter_ns()
    print(f"Part 2 took {END - START} nanoseconds")


if __name__ == '__main__':
    main()
        
