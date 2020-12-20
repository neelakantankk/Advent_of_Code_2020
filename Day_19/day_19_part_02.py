import re
import time

def parse_rule(rule,rules):
    if rule.isalpha():
        return rule
    elif mo:=re.match(r'^\d+$',rule):
        return f"{parse_rule(rules[rule],rules)}"
    elif mo:=re.search(r'^(.*?).[|].(.*?)$',rule):
        return f"({parse_rule(mo.group(1),rules)}|{parse_rule(mo.group(2),rules)})"
    elif mo:=re.findall(r'(\d+)',rule):
        output = ""
        for res in mo:
            output += f"{parse_rule(res,rules)}"
        return output
        

def main():
#    filename = 'example'
    filename = 'input'
    #filename = 'example2'

    START = time.perf_counter_ns()
    with open(filename,'r') as infile:
        rules,entries = (x.strip() for x in infile.read().split('\n\n'))

    rules = {k:v.strip().replace('"','') for k,v in (line.strip().split(":") for line in rules.split("\n"))}
    rules['8'] = ' 42 | 42 8'
    rules['11'] = '42 31 | 42 11 31'
    entries = [line.strip() for line in entries.split("\n")]

    matches = set()

    rule_42 = parse_rule(rules['42'],rules)
    rule_31 = parse_rule(rules['31'],rules)

    rule_8 = f"{rule_42}"

    for i in range(1,max(len(x) for x in entries)):
        rule_11 = f"({rule_42}){{{i}}}{rule_31}{{{i}}}"
        pattern = f"^({rule_8}+)({rule_11})$"
        for entry in entries:
            if mo:=re.search(pattern, entry):
                matches.add(entry)

    print(f"Matches: {len(matches)}")
    END = time.perf_counter_ns()
    print(f"Part 1 took {END - START} nanoseconds")

if __name__ == '__main__':
    main()
