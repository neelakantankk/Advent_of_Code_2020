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
    identified_dict = dict()
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
                ingredient = ingredients.pop()
                identified_ingredients.add(ingredient)
                identified_dict[allergen] = ingredient
            else:
                allergens[allergen] = ingredients - identified_ingredients
        for allergen in identified_allergens:
            if allergen in allergens.keys():
                allergens.pop(allergen)


    other_ingredients = set(all_ingredients) - identified_ingredients
    sorted_keys = sorted(identified_dict.keys())
    print(','.join(identified_dict[key] for key in sorted_keys))
    END = time.perf_counter_ns()
    print(f"Part 2 took {END - START} nanoseconds")

if __name__ == '__main__':
    main()
        
