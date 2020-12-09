from collections import deque

# File Input
try:
    input_file = open('input.txt')
except FileNotFoundError:
    input_file = open('day09/input.txt')

input = []

for line in input_file:
    input.append(int(line))

input_file.close()

preamble_size = 25

# Part 1 Solver
def first_invalid_number():
    # Create a deque with a maximum length of preamble_size
    prev_numbers = deque(input[0:preamble_size], preamble_size)

    for i in range(preamble_size, len(input)):
        valid = False

        # Check if this number is the sum of any 2 numbers in prev_numbers
        for j in range(preamble_size):
            for k in range(j + 1, preamble_size):
                if prev_numbers[j] + prev_numbers[k] == input[i]:
                    valid = True

        if not valid:
            return input[i]
        
        prev_numbers.append(input[i])

# Part 2 Solver
def find_encryption_weakness():
    target = first_invalid_number()

    for i in range(len(input)):
        number_chain = [input[i]]
        
        # Keep adding numbers until they sum to target or higher
        num1 = input[i]
        interval = 1

        if i + interval < len(input):
            num2 = input[i + interval]
        else:
            continue

        while num1 + num2 <= target:
            number_chain.append(num2)

            if sum(number_chain) == target:
                return min(number_chain) + max(number_chain)

            interval += 1
            num1 = num2
            num2 = input[i + interval]


print('Part 1 Answer:', first_invalid_number())
print('Part 2 Answer:', find_encryption_weakness())