# File Input
try:
    input_file = open('input.txt')
except FileNotFoundError:
    input_file = open('day14/input.txt')

input = []
highest_addr = 0

for line in input_file:
    if line.endswith('\n'):
        input.append(line[:-1])
    else:
        input.append(line)

input_file.close()


# Part 1 Solver
def part_one():
    # Initialise memory and bitmask
    mask = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
    memory = dict()

    for line in input:
        if line.startswith('mask'):
            mask = line[7:]
        elif line.startswith('mem'):
            address = int(line[4:line.find(']')])
            value = int(line[line.find('=') + 2:])

            # Convert value to binary
            bin_value = format(value, 'b').rjust(36, '0')
            modified_value = ''

            # Apply mask
            for i in range(len(mask)):
                if mask[i] == 'X':
                    modified_value += bin_value[i]
                else:
                    modified_value += mask[i]
            
            memory[address] = modified_value
    
    # Sum all values in memory
    sum = 0

    for addr in memory:
        # Convert to decimal
        bin_value = memory[addr].lstrip('0')
        dec_value = 0
        
        for i in range(len(bin_value)):
            dec_value += int(bin_value[-(i + 1)]) * 2**i

        # Add to sum
        sum += dec_value
    
    return sum


# Part 2 Solver
def part_two():
    # Initialise memory and bitmask
    mask = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
    memory = dict()
    
    for line in input:
        if line.startswith('mask'):
            mask = line[7:]
        elif line.startswith('mem'):
            address = int(line[4:line.find(']')])
            value = int(line[line.find('=') + 2:])

            # Convert address to binary
            bin_address = format(address, 'b').rjust(36, '0')
            modified_address = ''

            # Apply mask
            for i in range(len(mask)):
                if mask[i] == '0':
                    modified_address += bin_address[i]
                else:
                    modified_address += mask[i]

            # Write to all relevant addresses
            for addr in all_addresses(modified_address):
                memory[addr] = value
    
    # Calculate sum
    sum = 0

    for addr in memory:        
        sum += memory[addr]

    return sum


def all_addresses(floating_addr):
    """
    Takes a memory address containing 0s, 1s and Xs and recursively
    calculates all possibile substitutions of the Xs for 0s and 1s, and
    returns them as a list.
    """
    addresses = []

    if floating_addr.count('X') > 0:
        idx = floating_addr.rfind('X')

        # Recursively call this function with the last X swapped with a 0 and 1
        addresses += all_addresses(floating_addr[0:idx] + '0' + floating_addr[idx + 1:])
        addresses += all_addresses(floating_addr[0:idx] + '1' + floating_addr[idx + 1:])
    else:
        addresses.append(floating_addr)

    return addresses


print('Part 1 Answer:', part_one())
print('Part 2 Answer:', part_two())