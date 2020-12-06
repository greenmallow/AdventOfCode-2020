# File Input
try:
    input_file = open('input.txt')
except FileNotFoundError:
    input_file = open('day06/input.txt')

input = []

for line in input_file:
    input.append(line)

input_file.close()

# Modify the raw input so each group's details are all on only one line,
# and count the number of members in each group
forms = []
curr_form = ''

group_sizes = []
curr_group_size = 0

for i in range(len(input)):
    if input[i] != '\n' and i != len(input) - 1:
        curr_form += (input[i].rstrip())
        curr_group_size += 1
    else:
        # The last line in the file is a special case marking both
        # information and the end of a group
        if i == len(input) - 1:
            curr_form += (input[i].rstrip())
            curr_group_size += 1

        forms.append(curr_form)
        curr_form = ''

        group_sizes.append(curr_group_size)
        curr_group_size = 0


# Part 1 Solver
def count_anyone():
    # Remove duplicate questions from each line
    nodupl_forms = []

    for i in range(len(forms)):
        questions = {char for char in forms[i]}

        new_line = ''
        for question in questions:
            new_line += question

        nodupl_forms.append(new_line)

    # Find the count of times a question had 1/more 'yes' answer(s) in a group
    sum = 0

    for form in nodupl_forms:
        sum += len(form)
    
    return sum

# Part 2 Solver
def count_everyone():
    # Find the count of times a question had a 'yes' answer from every member
    # of a group
    sum = 0

    for i in range(len(forms)):
        questions = {char for char in forms[i]}

        for char in questions:
            if forms[i].count(char) == group_sizes[i]:
                sum += 1

    return sum


print('Part 1 Answer:', count_anyone())
print('Part 2 Answer:', count_everyone())

# Part 1 Solution: 6297
# Part 2 Solution: 3158