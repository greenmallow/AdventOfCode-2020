# File Input
try:
    input_file = open('input.txt')
except FileNotFoundError:
    input_file = open('day18/input.txt')

input = []

for line in input_file:
    if line.endswith('\n'):
        input.append(line[:-1])
    else:
        input.append(line)

input_file.close()


def solve_equation(equation, addition_first):
    """
    Solve an equation, using different rules of operator precedence.

    If addition_first is true, the equation will be solved by evaluating
    addition before multiplication. If it is false, the equation will be
    solved left-to-right, treating addition and multiplication as having
    the same precedence.
    """
    # If there are brackets remaining in the equation, we need to solve
    # the equation within those brackets first
    if equation.count('(') > 0:
        idx_start = equation.find('(') + 1

        # Find the first closing bracket
        next_close = equation.find(')', idx_start)

        # Count the number of opening brackets between the first opening
        # bracket and the first closing bracket
        inner_bracket_count = equation.count('(', idx_start, next_close)

        # Find the position of the opening and closing brackets
        if inner_bracket_count == 0:
            # The next closing bracket is the correct closing bracket
            idx_end = equation.find(')', idx_start)
        else:
            # Find the correct closing bracket
            i = 0
            while i < inner_bracket_count:
                idx_end = equation.find(')', next_close + 1)
                inner_bracket_count += equation[next_close + 1 : idx_end].count('(')

                next_close = idx_end
                i += 1

        # Replace the equation within the brackets with its answer
        inner_ans = solve_equation(equation[idx_start:idx_end], addition_first)
        equation = equation[:idx_start - 1] + str(inner_ans) + equation[idx_end + 1:]

        return solve_equation(equation, addition_first)
    else:
        # No brackets remaining, so we can solve the equation
        if addition_first:
            # Solve by evaluating addition before multiplication
            answer = solve_addition_first(equation)
        else:
            # Solve by treating addition and multiplication as having
            # the same precedence
            answer = solve_left_to_right(equation)

        return answer


def solve_addition_first(equation):
    """
    Evaluates an equation by performing addition before multiplication.

    Expects an equation string without brackets.
    """
    chunks = equation.split()

    # Split the equation into compoments separated by multiplications
    addition_eqs = []
    idx = 0
    start_of_eq = 0

    while idx < len(chunks):
        if chunks[idx] == '*':
            addition_eqs.append(chunks[start_of_eq : idx])
            
            start_of_eq = idx + 1
            idx += 2
        else:
            idx += 1
    
    addition_eqs.append(chunks[start_of_eq:])

    # Solve the addition equations, then multiply the answer by the
    # overall answer so far
    answer = 1

    for eq in addition_eqs:
        eq_answer = 0

        for component in eq:
            if component.isdecimal():
                eq_answer += int(component)
        
        answer *= eq_answer

    return answer


def solve_left_to_right(equation):
    """
    Evaluates an equation, treating addition and multiplication as
    having the same operator precedence.

    Expects an equation string without brackets.
    """
    chunks = equation.split()
    answer = int(chunks[0])

    idx = 0
    while idx < len(chunks):
        if chunks[idx].isdecimal():
            idx += 1
        elif chunks[idx] == '+':
            answer += int(chunks[idx + 1])
            idx += 2
        elif chunks[idx] == '*':
            answer *= int(chunks[idx + 1])
            idx += 2
        else:
            print(f'Unexpected token {chunks[idx]} was encountered. 0 was returned.')
            return 0

    return answer


# Part 1 Solver
def part_one():
    sum = 0

    for line in input:
        sum += solve_equation(line, False) 

    return sum

# Part 2 Solver
def part_two():
    sum = 0

    for line in input:
        sum += solve_equation(line, True) 

    return sum


print('Part 1 Answer:', part_one())
print('Part 2 Answer:', part_two())