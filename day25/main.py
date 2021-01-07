# Puzzle input
pub_key1 = 18499292
pub_key2 = 8790390


# Transform a subject number a given number of times
def transform(subj_num, loop_size):
    value = 1

    for i in range(loop_size):
        value *= subj_num
        value %= 20201227
    
    return value

# Get the number of iterations necessary to transform a subject number
# into a given target value
def get_loop_size(subj_num, target_val):
    value = 1
    loop_size = 0

    while value != target_val:
        loop_size += 1
        value *= subj_num
        value %= 20201227
    
    return loop_size


# Transform the second public key with the loop size of the first public
# key to produce the encryption key (the puzzle answer)
print('Answer:', transform(pub_key2, get_loop_size(7, pub_key1)))