# File Input
try:
    input_file = open('input.txt')
except FileNotFoundError:
    input_file = open('day21/input.txt')

input = []

for line in input_file:
    if line.endswith('\n'):
        input.append(line[:-1])
    else:
        input.append(line)

input_file.close()


# Create sets of all of the allergens and all of the ingredients that
# appear in the list of foods
all_allergens = set()
all_ingredients = set()

for food_list in input:
    components = food_list.split(' (contains ')
    ingredients = components[0].split()
    allergens = components[1][:-1].split(', ')

    for allergen in allergens:
        all_allergens.add(allergen)

    for ingredient in ingredients:
        all_ingredients.add(ingredient)


def get_possible_ingrs():
    """
    Create and return a dict which maps each allergen to a set of
    ingredients that could contain it
    """
    possible_ingrs = {allergen:all_ingredients.copy() for allergen in all_allergens}

    # Reduce the number of possible ingredients that contain each allergen
    for food_list in input:
        components = food_list.split(' (contains ')
        ingredients = set(components[0].split())
        allergens = components[1][:-1].split(', ')

        # The ingredient representing an allergen must be in every list
        # where it is mentioned, so if an ingredient is not in all lists
        # where an allergen is mentioned, it can't contain that allergen
        for allergen in allergens:
            possible_ingrs[allergen] = possible_ingrs[allergen].intersection(ingredients)
    
    return possible_ingrs


# Part 1 Solver
def part_one():
    possible_ingrs = get_possible_ingrs()
    
    # Create a set of ingredients that can't possibly contain any allergens
    no_allergen_ingrs = all_ingredients.copy()

    for allergen in all_allergens:
        no_allergen_ingrs = no_allergen_ingrs.difference(possible_ingrs[allergen])

    # Count the number of times to no-allergen ingredients appear in the
    # food lists
    count = 0

    for food_list in input:
        ingredients = food_list.split(' (contains ')[0].split()

        for ingr in ingredients:
            if ingr in no_allergen_ingrs:
                count += 1
    
    return count


# Part 2 Solver
def part_two():
    possible_ingrs = get_possible_ingrs()

    # Determine which ingredient containts which allergen
    while True:
        for allergen in all_allergens:
            if len(possible_ingrs[allergen]) == 1:
                # Remove that ingredient from the other allergens'
                # possibilities
                for allgn in all_allergens:
                    if allgn != allergen:
                        possible_ingrs[allgn] = possible_ingrs[allgn].difference(possible_ingrs[allergen])

        # Sum the lengths of each allergen's possible_ingrs set
        sum = 0
        for allergen in all_allergens:
            sum += len(possible_ingrs[allergen])
        
        # Loop until each allergen is mapped to one ingredient
        if sum == len(all_allergens):
            break
    
    # Create an alphabetically ordered list of allergens
    ordered_allergens = sorted(all_allergens)

    # Create the Canonical Dangerous Ingredient List (CDIL)
    cdil = ''
    for allergen in ordered_allergens:
        cdil += possible_ingrs[allergen].pop()
        cdil += ','

    # Return without the trailing comma
    return cdil[:-1]


print('Part 1 Answer:', part_one())
print('Part 2 Answer:', part_two())