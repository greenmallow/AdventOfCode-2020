# File Input
try:
    input_file = open('input.txt')
except FileNotFoundError:
    input_file = open('day16/input.txt')

input = []

for line in input_file:
    if line.endswith('\n'):
        input.append(line[:-1])
    else:
        input.append(line)

input_file.close()


class ValidRanges:
    """
    Encapsulates the ranges of values a field can take into a single
    object, with a method to check whether a number falls within those
    ranges or not.
    """
    def __init__(self, min1, max1, min2, max2):
        self.min1 = min1
        self.max1 = max1
        self.min2 = min2
        self.max2 = max2
    
    def can_contain(self, num):
        if (num >= self.min1 and num <= self.max1) or (num >= self.min2 and num <= self.max2):
            return True
        else:
            return False


# Store rules for ticket fields in a dict and create a set of values
# that are valid for at least one field.
fields = dict()
valid_for_some_field = set()

line = 0
while input[line] != '':
    data = input[line].split(': ')
    field = data[0] # Name of the field
    ranges = data[1].split(' or ')
    range_values = [] # The minimum and maximum values of each range

    for rng in ranges:
        values = rng.split('-')
        min = int(values[0])
        max = int(values[1])

        # Add to the set of numbers that are valid in >=1 field
        for i in range(min, max + 1):
            valid_for_some_field.add(i)
        
        range_values += [min, max]
    
    # Store field info in the fields dict
    fields[field] = ValidRanges(range_values[0], range_values[1], 
        range_values[2], range_values[3])

    line += 1


# Part 1 Solver
def part_one():
    tse_rate = 0
    
    for line in input[input.index('nearby tickets:') + 1:]:
        values = line.split(',')

        for value in values:
            value = int(value)

            if value not in valid_for_some_field:
                tse_rate += value
    
    return tse_rate


# Part 2 Solver
def part_two():
    start_of_nearby_tickets = input.index('nearby tickets:') + 1

    # Create a list containing only tickets without invalid values
    valid_tickets = []

    for i in range(start_of_nearby_tickets, len(input)):
        values = input[i].split(',')
        valid = True

        for value in values:
            value = int(value)

            if value not in valid_for_some_field:
                valid = False
                break

        if valid:
            valid_tickets.append(input[i])
    
    # Map each position to what fields it could potentially be
    potential_fields = dict()

    for i in range(len(fields)):
        potentials = list(fields)
        fields_to_remove = set()

        # Determine which fields cannot represent position i
        for ticket in valid_tickets:
            value = int(ticket.split(',')[i])

            for field in potentials:
                if not fields[field].can_contain(value):
                    fields_to_remove.add(field)
        
        # Remove the invalid fields from the list of potential fields
        for field in fields_to_remove:
            potentials.remove(field)
        
        # Store this position's potential fields in the dict
        potential_fields[i] = potentials

    
    # Reduces the list of potential fields in each position to 1 by
    # looking at which fields have already been determined and removing
    # those fields from the other positions' lists until each position
    # can only be represented by one field.
    determined_fields = dict()

    # When sum_potentials == len(fields), each position has one field
    # associated with it
    sum_potentials = 0
    for pos in potential_fields:
        sum_potentials += len(potential_fields[pos])
    
    
    while sum_potentials > len(fields):
        determined_field = ''

        for i in range(len(potential_fields)):
            if len(potential_fields[i]) == 1 and i not in determined_fields:
                determined_field = potential_fields[i][0]

                determined_fields[i] = determined_field

                # Remove the already-determined field from the other
                # fields' lists of potential fields
                for j in range(len(potential_fields)):
                    if determined_field in potential_fields[j] and j != i:
                        potential_fields[j].remove(determined_field)
                        
                # Recalculate how many potential fields are remaining
                # across all positions
                sum_potentials = 0
                for pos in potential_fields:
                    sum_potentials += len(potential_fields[pos])
                
                break
    
    # Find the product of the values in the six departure-related 
    # fields in my ticket
    my_ticket = input[input.index('your ticket:') + 1].split(',')
    product = 1

    for field in determined_fields:
        if determined_fields[field].startswith('departure'):
            product *= int(my_ticket[field])

    return product


print('Part 1 Answer:', part_one())
print('Part 2 Answer:', part_two())