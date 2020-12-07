import re
import pprint

def parse_line(line):
    mo = re.search(r"^(.*?) bags contain (.*?)$", line)
    key = mo.group(1)
    value = re.findall(r'(\d+) (\w+ \w+) bag',mo.group(2))
    return (key,value)



def main():
    
    with open('input','r') as infile:
        entries = [line.strip() for line in infile.readlines()]
    
    rules = {key:value for key,value in [parse_line(line) for line in entries]}

    def contains_shiny_gold(bag):
        if rules[bag] == []:
            return False
        elif 'shiny gold' in [x[1] for x in rules[bag]]:
            return True
        else:
            contains_bag = False
            for inner_bag in rules[bag]:
                contains_bag = contains_bag or contains_shiny_gold(inner_bag[1])
            return contains_bag

    def get_all_bags_in_bag(bag):
        if rules[bag] == []:
            return 0
        else:
            sum_bags = 0
            for inner_bag in rules[bag]:
                sum_bags += (int(inner_bag[0])*get_all_bags_in_bag(inner_bag[1])) 
            return sum_bags + sum([int(bag[0]) for bag in rules[bag]])


    count_of_bags = 0
    for bag in rules.keys():
        if contains_shiny_gold(bag):
            count_of_bags+=1

    print(count_of_bags)
    print(get_all_bags_in_bag('shiny gold'))

if __name__ == '__main__':
    main()

