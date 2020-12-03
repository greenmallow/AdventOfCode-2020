# File Input
try:
    input_file = open('input.txt')
except FileNotFoundError:
    input_file = open('day03/input.txt')

input = []

for line in input_file:
    input.append(line)

input_file.close()

def trees_encountered(right, down):
    row = 0
    col = 0
    tree_count = 0

    while row < len(input):
        if input[row][col] == '#':
            tree_count += 1
        
        # len(input[0]) includes the newline character, so 1 must be subtracted from it.
        col = (col + right) % (len(input[0]) - 1)
        row += down

    return tree_count


print('Part 1 Answer:', trees_encountered(3, 1))

# Part 2
r1d1 = trees_encountered(1, 1)
r3d1 = trees_encountered(3, 1)
r5d1 = trees_encountered(5, 1)
r7d1 = trees_encountered(7, 1)
r1d2 = trees_encountered(1, 2)

product = r1d1 * r3d1 * r5d1 * r7d1 * r1d2
print('Part 2 Answer:', product)

# Part 1 Solution: 289
# Part 2 Solution: 5522401584