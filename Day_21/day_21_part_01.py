import re
from functools import reduce
import time

def main():
    filename = 'input'
#    filename = 'example'
    
    START = time.perf_counter_ns()
    with open(filename, 'r') as infile:
        lines = [line.strip() for line in infile.readlines()]

    allergens = dict()
    identified_ingredients = set()
    identified_allergens = set()
    all_ingredients = list()
    for line in lines:
        mo = re.search(r'^(.*?)\(contains (.*?)\)',line)
        ingredients = set(mo.group(1).strip().split(" "))
        current_allergens = set(allergen.strip() for allergen in mo.group(2).strip().split(",")) 
        all_ingredients.extend(ingredients)
        for allergen in current_allergens:
            allergens[allergen] = allergens.get(allergen,ingredients).intersection(ingredients)

    while len(allergens.keys()) != 0:
        for allergen,ingredients in allergens.items():
            if len(ingredients) == 1:
                identified_allergens.add(allergen)
                identified_ingredients.add(ingredients.pop())
            else:
                allergens[allergen] = ingredients - identified_ingredients
        for allergen in identified_allergens:
            if allergen in allergens.keys():
                allergens.pop(allergen)
    other_ingredients = set(all_ingredients) - identified_ingredients
    count_of_appearances = reduce(lambda x,y:x+y,(all_ingredients.count(x) for x in other_ingredients))
    print(count_of_appearances)
    END = time.perf_counter_ns()
    print(f"Part 1 took {END - START} nanoseconds")

if __name__ == '__main__':
    main()
        
