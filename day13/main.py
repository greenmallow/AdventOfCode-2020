# File Input
try:
    input_file = open('input.txt')
except FileNotFoundError:
    input_file = open('day13/input.txt')

input = []

for line in input_file:
    if line.endswith('\n'):
        input.append(line[:-1])
    else:
        input.append(line)

input_file.close()


earliest_dep = int(input[0])
buses = input[1].split(',')

buses_in_service = []
for bus in buses:
    if bus != 'x':
        buses_in_service.append(int(bus))


# Part 1 Solver
def part_one():
    first_dep = dict()
    
    # Map bus IDs to their first departure at or after earliest_dep
    for bus in buses_in_service:
        # This is calculated in two stages to allow for the fact that a
        # bus could be due to depart at exactly earliest_dep
        first_dep[bus] = bus * (earliest_dep // bus)

        if first_dep[bus] < earliest_dep:
            first_dep[bus] += bus
    
    # Set earliest_bus to above the highest value it could be
    earliest_bus_id = -1
    earliest_bus_time = earliest_dep + max(buses_in_service)

    # Determine which bus leaves first
    for bus in first_dep:
        if first_dep[bus] <= earliest_bus_time:
            earliest_bus_id = bus
            earliest_bus_time = first_dep[earliest_bus_id]
    
    return earliest_bus_id * (first_dep[earliest_bus_id] - earliest_dep)


print('Part 1 Answer:', part_one())
# print('Part 2 Answer:', part_two())