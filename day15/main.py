import time

starting_nums = [14, 3, 1, 0, 9, 5]

def memory_game(turns_to_play):
    # Dict mapping a number to the last two turns on which it was spoken
    turns_spoken = dict()
    turn = 0
    last_spoken = None

    # Read the starting numbers
    for num in starting_nums:
        turn += 1

        if last_spoken != None:
            turns_spoken[last_spoken] = [turn - 1, None]
        
        last_spoken = num
    
    # Continue the game for the provided number of turns
    while turn < turns_to_play:
        turn += 1

        if last_spoken in turns_spoken:
            # Update the dict
            turns_spoken[last_spoken][1] = turns_spoken[last_spoken][0]
            turns_spoken[last_spoken][0] = turn - 1

            # Calculate number to say
            last_spoken = turns_spoken[last_spoken][0] - turns_spoken[last_spoken][1]

        else:
            # First time the number was said
            turns_spoken[last_spoken] = [turn - 1, None]

            last_spoken = 0
    
    return last_spoken


print('Part 1 Answer:', memory_game(2020))

start = time.time()
print('Part 2 Answer:', memory_game(30000000))
print('Part 2 completed in', round(time.time() - start, 4), 'seconds.')