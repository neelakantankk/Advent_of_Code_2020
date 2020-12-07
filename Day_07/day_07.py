import re
import pprint

def parse_line(line):
    mo = re.search(r"^(.*?) bags contain (.*?)$", line)
    key = mo.group(1)
    value = re.findall(r'\d+ (\w+ \w+) bag',mo.group(2))
    return (key,value)



def main():
    
    with open('input','r') as infile:
        entries = [line.strip() for line in infile.readlines()]
    
    rules = {key:value for key,value in [parse_line(line) for line in entries]}

    def contains_shiny_gold(bag):
        if rules[bag] == []:
            return False
        elif 'shiny gold' in rules[bag]:
            return True
        else:
            contains_bag = False
            for inner_bag in rules[bag]:
                contains_bag = contains_bag or contains_shiny_gold(inner_bag)
            return contains_bag

    count_of_bags = 0
    for bag in rules.keys():
        if contains_shiny_gold(bag):
            count_of_bags+=1

    print(count_of_bags)








if __name__ == '__main__':
    main()

