# File Input
try:
    input_file = open('input.txt')
except FileNotFoundError:
    input_file = open('day12/input.txt')

input = []

for line in input_file:
    if line.endswith('\n'):
        input.append(line[:-1])
    else:
        input.append(line)

input_file.close()


# Part 1 Solver
def part_one():
    # North and east are positive, south and west are negative
    ns_pos = 0
    ew_pos = 0
    dir_facing = 90 # 0 = North, 90 = East, 180 = South, 270 = West

    for instruction in input:
        action = instruction[0]
        value = int(instruction[1:])

        if action == 'N':
            ns_pos += value
        elif action == 'S':
            ns_pos -= value
        elif action == 'E':
            ew_pos += value
        elif action == 'W':
            ew_pos -= value
        elif action == 'L':
            dir_facing = (dir_facing - value) % 360
        elif action == 'R':
            dir_facing = (dir_facing + value) % 360
        elif action == 'F':
            if dir_facing == 0: # Go north
                ns_pos += value
            elif dir_facing == 90: # Go east
                ew_pos += value
            elif dir_facing == 180: # Go south
                ns_pos -= value
            elif dir_facing == 270: # Go east
                ew_pos -= value
    
    # Calculate Manhattan distance from starting point
    manhattan_dist = abs(ns_pos) + abs(ew_pos)
    return manhattan_dist


# Part 2 Solver
def part_two():
    # North and east are positive, south and west are negative
    ship_ns_pos = 0
    ship_ew_pos = 0
    waypoint_ns_pos = 1
    waypoint_ew_pos = 10

    for instruction in input:
        action = instruction[0]
        value = int(instruction[1:])

        if action == 'N':
            waypoint_ns_pos += value
        elif action == 'S':
            waypoint_ns_pos -= value
        elif action == 'E':
            waypoint_ew_pos += value
        elif action == 'W':
            waypoint_ew_pos -= value
        elif action == 'L':
            # Rotates the waypoint around the ship left (anti-clockwise)
            rotations = value // 90

            for i in range(rotations):
                prev_positions = [waypoint_ns_pos, waypoint_ew_pos]
                waypoint_ew_pos = -prev_positions[0]
                waypoint_ns_pos = prev_positions[1]

        elif action == 'R':
            # Rotates the waypoint around the ship right (clockwise)
            rotations = value // 90

            for i in range(rotations):
                prev_positions = [waypoint_ns_pos, waypoint_ew_pos]
                waypoint_ew_pos = prev_positions[0]
                waypoint_ns_pos = -prev_positions[1]

        elif action == 'F':
            ship_ew_pos += (value * waypoint_ew_pos)
            ship_ns_pos += (value * waypoint_ns_pos)
    
    # Calculate Manhattan distance from starting point
    manhattan_dist = abs(ship_ns_pos) + abs(ship_ew_pos)
    return manhattan_dist


print('Part 1 Answer:', part_one())
print('Part 2 Answer:', part_two())