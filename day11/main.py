import time

# File Input
try:
    input_file = open('input.txt')
except FileNotFoundError:
    input_file = open('day11/input.txt')

input = []

for line in input_file:
    if line.endswith('\n'):
        input.append(line[:-1])
    else:
        input.append(line)

input_file.close()

seats = input.copy()


# Counts the number of occupied seats among those immediately adjacent
# to the seat at (row, col) (for Part 1)
def adjacent_seats_occupied(row, col):
    occupied = 0

    for r in range(row - 1, row + 2):
        for c in range(col - 1, col + 2):
            # Skip the seat we are checking the neighbours of
            if r == row and c == col:
                continue

            # Python has negative indexing, but we don't want to check
            # positions on the other side of the grid
            if r < 0 or r >= len(seats) or c < 0 or c >= len(seats[row]):
                continue
            
            if seats[r][c] == '#':
                occupied += 1

    return occupied


# Counts the number of occupied seats among those that are the first
# visible seat in each direction from the seat at (row, col) (for Part 2)
def visible_seats_occupied(row, col):
    occupied = 0

    for lr_increment in range(-1, 2):
        for ud_increment in range (-1, 2):
            # Skip the seat we are looking from
            if lr_increment == 0 and ud_increment == 0:
                continue
            
            r = row + lr_increment
            c = col + ud_increment

            if r < 0 or r >= len(seats) or c < 0 or c >= len(seats[row]):
                continue

            first_visible = seats[r][c]

            # If the next seat is the floor, keep looking until a seat
            # is found or the edge is reached
            while first_visible == '.':
                r += lr_increment
                c += ud_increment

                if r < 0 or r >= len(seats) or c < 0 or c >= len(seats[row]):
                    break

                first_visible = seats[r][c]
            
            if first_visible == '#':
                occupied += 1

    return occupied


# Part 1 Solver
def occupied_seats_p1():
    global seats
    next_seats = []

    for row in seats:
        next_seats.append('')

    first_time = True

    while seats != next_seats:
        if not first_time:
            seats = next_seats.copy()
        else:
            first_time = False

        for row in range(len(seats)):
            new_row = ''
            for col in range(len(seats[row])):
                # The floor never changes
                if seats[row][col] == '.':
                    new_row += '.'
                    continue

                adj_occupied_seats = adjacent_seats_occupied(row, col)

                # Implementation of rules
                if seats[row][col] == 'L' and adj_occupied_seats == 0:
                    new_row += '#'
                elif seats[row][col] == '#' and adj_occupied_seats >= 4:
                    new_row += 'L'
                else:
                    new_row += seats[row][col]
            
            next_seats[row] = new_row
    
    # Calculate how many seats remain occupied
    seats_occupied = 0

    for row in seats:
        seats_occupied += row.count('#')

    return seats_occupied


# Part 2 Solver
def occupied_seats_p2():
    global seats
    next_seats = []

    for row in seats:
        next_seats.append('')

    first_time = True

    while seats != next_seats:
        if not first_time:
            seats = next_seats.copy()
        else:
            first_time = False

        for row in range(len(seats)):
            new_row = ''

            for col in range(len(seats[row])):
                # The floor never changes
                if seats[row][col] == '.':
                    new_row += '.'
                    continue

                vis_occupied_seats = visible_seats_occupied(row, col)

                # Implementation of rules
                if seats[row][col] == 'L' and vis_occupied_seats == 0:
                    new_row += '#'
                elif seats[row][col] == '#' and vis_occupied_seats >= 5:
                    new_row += 'L'
                else:
                    new_row += seats[row][col]
            
            next_seats[row] = new_row
    
    # Calculate how many seats remain occupied
    seats_occupied = 0

    for row in seats:
        seats_occupied += row.count('#')

    return seats_occupied


# Run Part 1 with timing
print('Part 1 commenced.')
start_time = time.time()
print('Part 1 Answer:', occupied_seats_p1())
end_time = time.time()
print('Part 1 time:', round(end_time - start_time, 4), 'seconds.', end = '\n\n')

# Reset the seat grid
seats = input.copy()

# Run Part 2 with timing
print('Part 2 commenced.')
start_time = time.time()
print('Part 2 Answer:', occupied_seats_p2())
end_time = time.time()
print('Part 2 time:', round(end_time - start_time, 4), 'seconds.')