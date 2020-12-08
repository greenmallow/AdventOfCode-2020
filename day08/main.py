# File Input
try:
    input_file = open('input.txt')
except FileNotFoundError:
    input_file = open('day08/input.txt')

instructions = []

for line in input_file:
    instructions.append(line)

input_file.close()


"""
Executes a list of instructions, returning the values of the accumulator
and next_instr when the program either terminates or is about to begin
an infinite loop.
"""
def run_boot_code(instructions):
    accumulator = 0
    executed_instrs = []

    # Run the program until an instruction is about to be executed a 2nd time
    next_instr = 0

    while next_instr not in executed_instrs:
        # Check if the program is supposed to terminate
        if next_instr == len(instructions):
            return accumulator, next_instr

        # Record that this instruction was executed
        executed_instrs.append(next_instr)

        operation = instructions[next_instr].split()[0]
        argument = instructions[next_instr].split()[1]

        if operation == 'nop':
            next_instr += 1
        elif operation == 'acc':
            accumulator += int(argument)
            next_instr += 1
        elif operation == 'jmp':
            next_instr += int(argument)
    
    # Return the accumulator value before an infinite loop begins and
    # the instruction that would be the start of the loop
    return accumulator, next_instr
    

# Part 2 Solver
def fixed_program_result():
    for i in range(len(instructions)):
        operation = instructions[i].split()[0]
        altered_instructions = instructions.copy()

    	# Modify one instruction in the list
        if operation == 'nop':
            altered_instructions[i] = 'jmp ' + instructions[i].split()[1]
        elif operation == 'jmp':
            altered_instructions[i] = 'nop ' + instructions[i].split()[1]
            
        result = run_boot_code(altered_instructions)
        
        if result[1] == len(instructions):
            return result[0]
    

print('Part 1 Answer:', run_boot_code(instructions)[0])
print('Part 2 Answer:', fixed_program_result())