# File Input
input_file = open('day01/input.txt')

input = []

for line in input_file:
    input.append(int(line))

input_file.close()


# Part 1 Solver
for i in range(len(input)):
    for j in range(i, len(input)):
        if input[i] + input[j] == 2020:
            result = input[i] * input[j]

            print(f'{input[i]} and {input[j]} sum to 2020 and multiply to {result}')
            break

# Part 2 Solver
for i in range(len(input)):
    for j in range(i, len(input)):
        for k in range(j, len(input)):
            if input[i] + input[j] + input[k] == 2020:
                result = input[i] * input[j] * input[k]

                print(f'{input[i]}, {input[j]} & {input[k]} sum to 2020 and multiply to {result}')
                break

# Part 1 Solution: 1011 & 1009 sum to 2020 and multiply to 1020099
# Part 2 Solution: 1434, 520 & 66 sum to 2020 and multiply to 49214880