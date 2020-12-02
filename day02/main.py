# File Input
input_file = open('day02/input.txt')

input = []

for line in input_file:
    input.append(line)

input_file.close()

# Split each line into a list containing policy, character & password
for i in range(len(input)):
    input[i] = input[i].split()

# Part 1 Solver
def count_valid_p1():
    count_valid = 0

    for password in input:
        # Get minimum and maximum times the letter must appear
        occurrences = password[0].split('-')
        min = int(occurrences[0])
        max = int(occurrences[1])

        # Get character to look for (first character in password[1])
        char = password[1][0]

        # Check if character appears the correct number of times
        char_count = password[2].count(char)

        if char_count >= min and char_count <= max:
            count_valid += 1
        
    return count_valid

# Part 2 Solver
def count_valid_p2():
    count_valid = 0

    for password in input:
        # Get positions to check and adjust indexing
        positions = password[0].split('-')
        index1 = int(positions[0]) - 1
        index2 = int(positions[1]) - 1

        # Get character to look for (first character in password[1])
        char = password[1][0]

        # Check if the character only appears in one position
        appearances = 0

        if password[2][index1] == char:
            appearances += 1
        
        if password[2][index2] == char:
            appearances += 1
        
        if appearances == 1:
            count_valid += 1

    return count_valid


print('Part 1 Answer:', count_valid_p1())
print('Part 2 Answer:', count_valid_p2())

# Part 1 Solution: 515
# Part 2 Solution: 711