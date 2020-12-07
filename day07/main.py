# File Input
try:
    input_file = open('input.txt')
except FileNotFoundError:
    input_file = open('day07/input.txt')

input = []

for line in input_file:
    input.append(line)

input_file.close()

# Create dict of rules mapping bag colours to what bags they contain
rules = dict()

for line in input:
    rule = line.split(' bags contain ')

    contents = rule[1].rstrip('.\n').split(', ')
    rules[rule[0]] = contents


# Part 1 Solver
def num_colours(target_colour):
    permitted_containers = set()

    # Find colours that can directly hold target_colour
    for colour in rules:
        for item in rules[colour]:
            if target_colour in item:
                permitted_containers.add(colour)

    # Find colours that can indirectly hold target_colour
    new_colours = permitted_containers.copy()

    while len(new_colours) > 0:
        extras = set()

        # Look for new_colours in rules
        for nc in new_colours:
            for colour in rules:
                for item in rules[colour]:
                    if nc in item:
                        extras.add(colour)
        
        permitted_containers = permitted_containers.union(extras)
        new_colours = extras.copy()

    return len(permitted_containers)

# Part 2 Solver
def bags_inside(target_colour):
    num_contained_bags = 0
    contents = rules[target_colour]

    for item in contents:
        num_contained_bags += contained_bags(item)

    return num_contained_bags

def contained_bags(item):
    if item == 'no other bags':
        return 0
    else:
        num_contained_bags = 0

        # Get number of bags contained
        num_bags = int(item.split(' ', 1)[0])
        num_contained_bags += num_bags

        # Get number of sub-contained bags
        colour = item.split(' ', 1)[1].rstrip('bags').rstrip()

        for sub_item in rules[colour]:
            num_contained_bags += num_bags * contained_bags(sub_item)

        return num_contained_bags


print('Part 1 Answer:', num_colours('shiny gold'))
print('Part 2 Answer:', bags_inside('shiny gold'))