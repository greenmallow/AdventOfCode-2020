# File Input
try:
    input_file = open('input.txt')
except FileNotFoundError:
    input_file = open('day10/input.txt')

input = []

for line in input_file:
    input.append(int(line))

input_file.close()


# Sorting the the input from smallest to largest makes it much easier to deal with
input.sort()
max_adapter_rating = input[-1]


# Part 1 Solver
def part_one():
    joltage_diff_distrib = {1:0, 2:0, 3:0}

    # Account for charging outlet
    joltage_diff_distrib[input[0]] += 1
    
    for i in range(len(input) - 1):
        next_rating = input[i + 1]

        joltage_diff_distrib[next_rating - input[i]] += 1

    # Account for device's built-in adapter
    joltage_diff_distrib[3] += 1

    return joltage_diff_distrib[1] * joltage_diff_distrib[3]


# Part 2 Solver
def part_two():
    arrangements_after = dict()

    for adapter in input:
        arrangements_after[adapter] = 0
    
    # The charging outlet (0 jolts) also needs to be included
    arrangements_after[0] = 0

    # Only one possible arrangement after the highest input is reached
    arrangements_after[max_adapter_rating] = 1

    # Create a copy of the inputs which will be iterated through in reverse order
    reversed_input = input.copy()
    reversed_input.reverse()
    reversed_input.append(0) # To factor in charging port
    
    # Skip index 0 as it has already been set to 1
    for adapter in reversed_input[1:]:
        if adapter + 1 in input:
            arrangements_after[adapter] += arrangements_after[adapter + 1]
        
        if adapter + 2 in input:
            arrangements_after[adapter] += arrangements_after[adapter + 2]
        
        if adapter + 3 in input:
            arrangements_after[adapter] += arrangements_after[adapter + 3]
    
    return arrangements_after[0]


print('Part 1 Answer:', part_one())
print('Part 2 Answer:', part_two())