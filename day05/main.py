# File Input
try:
    input_file = open('input.txt')
except FileNotFoundError:
    input_file = open('day05/input.txt')

input = []

for line in input_file:
    input.append(line)

input_file.close()

# Constants
MAX_ROW_ID = 127
MAX_COL_ID = 7

# Seat ID Calculator
def calc_seat_id(seat):
    # Find row
    min = 0
    max = MAX_ROW_ID

    for char in seat[0:7]:
        range = (max - min) + 1

        if char == 'F':
            max -= range / 2
        elif char == 'B':
            min += range / 2
    
    row = int(min)

    # Find column
    min = 0
    max = MAX_COL_ID

    for char in seat[7:10]:
        range = (max - min) + 1

        if char == 'L':
            max -= range / 2
        elif char == 'R':
            min += range / 2
    
    col = int(min)

    # Calculate and return seat ID
    return (row * 8) + col

# Part 1 Solver
def highest_seat_id():
    highest_id = -1

    for seat in input:
        seat_id = calc_seat_id(seat)

        if seat_id > highest_id:
            highest_id = seat_id

    return highest_id

# Part 2 Solver
def find_missing_seat():
    seat_ids = []
    missing_seat_id = -1

    for seat in input:
        seat_ids.append(calc_seat_id(seat))
    
    for i in range((MAX_ROW_ID * 8) + MAX_COL_ID):
        if i not in seat_ids:
            if i - 1 in seat_ids and i + 1 in seat_ids:
                missing_seat_id = i
    
    return missing_seat_id


print('Part 1 Answer:', highest_seat_id())
print('Part 2 Answer:', find_missing_seat())

# Part 1 Solution: 871
# Part 2 Solution: 640