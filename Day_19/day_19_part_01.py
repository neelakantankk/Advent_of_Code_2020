import re
import time

def parse_rule(rule,rules):
    if rule.isalpha():
        return rule
    elif mo:=re.match(r'^\d+$',rule):
        return f"({parse_rule(rules[rule],rules)})"
    elif mo:=re.search(r'^(.*?).[|].(.*?)$',rule):
        return f"({parse_rule(mo.group(1),rules)}|{parse_rule(mo.group(2),rules)})"
    elif mo:=re.findall(r'(\d+)',rule):
        output = "("
        for res in mo:
            output += f"({parse_rule(res,rules)})"
        output += ")"
        return output
        

def main():
    filename = 'example'
    filename = 'input'

    START = time.perf_counter_ns()
    with open(filename,'r') as infile:
        rules,entries = (x.strip() for x in infile.read().split('\n\n'))

    rules = {k:v.strip().replace('"','') for k,v in (line.strip().split(":") for line in rules.split("\n"))}
    entries = (line.strip() for line in entries.split("\n"))

    pattern = f"^{parse_rule(rules['0'],rules)}$"
    matches = 0

    for entry in entries:
        if re.search(pattern,entry):
            matches+=1

    print(f"Matches: {matches}")
    END = time.perf_counter_ns()
    print(f"Part 1 took {END - START} nanoseconds")

if __name__ == '__main__':
    main()
