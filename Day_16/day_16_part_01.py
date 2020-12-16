import re
import sys

def main():

    filename = 'example'
    filename = 'input'
    with open(filename,'r') as infile:
        notes = [line.strip() for line in infile.read().split("\n\n")]

    valid_values = set()

    for field_notes in notes[0].split("\n"):
        mo = re.compile(r'^(?P<field>.*?): (\d+)-(\d+) or (\d+)-(\d+)')
        result = mo.search(field_notes)
        low1 = int(result.group(2))
        high1 = int(result.group(3))
        low2 = int(result.group(4))
        high2 = int(result.group(5))
        valid_values.update(i for i in range(low1,high1+1))
        valid_values.update(i for i in range(low2,high2+1))


    invalid_values = []

    for field_notes in notes[2].split("\n")[1:]:
        nums = [int(i) for i in field_notes.split(",")]
        invalid_values.extend(i for i in nums if i not in valid_values)

    print(sum(invalid_values))

if __name__ == '__main__':
    main()
        
