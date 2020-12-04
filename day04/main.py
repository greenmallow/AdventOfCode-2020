# File Input
try:
    input_file = open('input.txt')
except FileNotFoundError:
    input_file = open('day04/input.txt')

input = []

for line in input_file:
    input.append(line)

input_file.close()

# Modify the raw input so each passport's details are all on only one line
passports = []
curr_passport = ''

for i in range(len(input)):
    if input[i] != '\n' and i != len(input) - 1:
        curr_passport += (input[i].rstrip() + ' ')
    else:
        # The last line in the file is a special case marking both
        # information and the end of a passport
        if i == len(input) - 1:
            curr_passport += (input[i].rstrip() + ' ')

        passports.append(curr_passport)
        curr_passport = ''


# Validates that all expected fields are present in a passport
def validate_fields(passport):
    is_valid = True
    expected_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

    full_fields = passport.split()

    # Create a list of the fields present in the passport
    present_fields = [field.split(':')[0] for field in full_fields]

    # Check that each expected field is actually in the passport
    for field in expected_fields:
        if field not in present_fields:
            is_valid = False
    
    return is_valid  


# Part 1 Solver
def count_valid_passports_p1():
    count_valid = 0

    for passport in passports:
        if validate_fields(passport):
            count_valid += 1        

    return count_valid
    

# Part 2 Solver
def count_valid_passports_p2():
    count_valid = 0

    for passport in passports:
        is_valid = True

        # Validate the provided fields
        if not validate_fields(passport):
            is_valid = False  
            continue # Passport is already deemed invalid

        full_fields = passport.split()

        # Validate birth year
        for field in full_fields:
            if field.startswith('byr'):
                year = int(field.split(':')[1])

                if year < 1920 or year > 2002:
                    is_valid = False
        
        # Validate issue year
        for field in full_fields:
            if field.startswith('iyr'):
                year = int(field.split(':')[1])

                if year < 2010 or year > 2020:
                    is_valid = False
        
        # Validate expiration year
        for field in full_fields:
            if field.startswith('eyr'):
                year = int(field.split(':')[1])

                if year < 2020 or year > 2030:
                    is_valid = False
        
        # Validate height
        for field in full_fields:
            if field.startswith('hgt'):
                height = field.split(':')[1]

                if height.endswith('cm'):
                    value = int(height.removesuffix('cm'))

                    if value < 150 or value > 193:
                        is_valid = False
                elif height.endswith('in'):
                    value = int(height.removesuffix('in'))

                    if value < 59 or value > 76:
                        is_valid = False
                else:
                    is_valid = False
        
        # Validate hair colour
        for field in full_fields:
            if field.startswith('hcl'):
                colour_code = field.split(':')[1]
                
                if colour_code.startswith('#'):
                    for char in colour_code.lstrip('#'):
                        if char not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']:
                            is_valid = False
                else:
                    is_valid = False
        
        # Validate eye colour
        for field in full_fields:
            if field.startswith('ecl'):
                colour = field.split(':')[1]
                
                if colour not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
                    is_valid = False
        
        # Validate passport ID
        for field in full_fields:
            if field.startswith('pid'):
                # Check that the ID is a number
                try:
                    pid = int(field.split(':')[1])
                except ValueError:
                    is_valid = False
                
                # Check the length of the ID
                pid = field.split(':')[1] # Reset 'pid' to include leading zeros
                
                if len(pid) != 9:
                    is_valid = False

        if is_valid:
            count_valid += 1        

    return count_valid


print('Part 1 Answer:', count_valid_passports_p1())
print('Part 2 Answer:', count_valid_passports_p2())

# Part 1 Solution: 202
# Part 2 Solution: 137