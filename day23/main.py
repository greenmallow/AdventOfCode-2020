from collections import deque

# Input
input = '952438716'
init_cups = deque()

for cup in input:
    init_cups.append(int(cup))

min_cup = min(init_cups)
max_cup = max(init_cups)


# Part 1 Solver
def part_one():
    cups = init_cups.copy()

    for i in range(100):
        current_cup = cups.popleft()
        
        # Pick up next three cups
        next_three = []
        for j in range(3):
            next_three.append(cups.popleft())
        
        # Select destination cup
        dest_cup = current_cup - 1

        while dest_cup in next_three or dest_cup < min_cup:
            dest_cup -= 1
            
            if dest_cup < min_cup:
                dest_cup = max_cup
        
        # Place picked up cups after destination cup
        dest_idx = cups.index(dest_cup)
        for i in range(len(next_three)):
            cups.insert(dest_idx + i + 1, next_three[i])

        # Add the current cup back to the list
        cups.append(current_cup)
    
    # Produce the answer string
    answer = ''

    # Find where the '1' cup is, shift the cups so that the '1' is at
    # the end, then remove it from the deque
    one_index = cups.index(1)
    cups.rotate(len(cups) - one_index - 1)
    cups.pop()

    for cup in cups:
        answer += str(cup)

    return answer


# Part 2 Solver
def part_two():
    pass


print('Part 1 Answer:', part_one())
print('Part 2 Answer:', part_two())