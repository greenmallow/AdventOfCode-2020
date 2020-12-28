from collections import deque

# File Input
try:
    input_file = open('input.txt')
except FileNotFoundError:
    input_file = open('day22/input.txt')

input = []

for line in input_file:
    if line.endswith('\n'):
        input.append(line[:-1])
    else:
        input.append(line)

input_file.close()


# The 'top card' is considered to be the leftmost card in the deque
p1_init_deck = deque()
p2_init_deck = deque()

# Find the gap in the input between the two decks
for i in range(len(input)):
    if input[i] == '':
        deck_break = i
        break

# Fill Player 1's deck
for line in input[1:deck_break]:
    p1_init_deck.append(int(line))

# Fill Player 2's deck
for line in input[deck_break + 2:]:
    p2_init_deck.append(int(line))


# Part 1 Solver
def play_combat():
    p1_deck = p1_init_deck.copy()
    p2_deck = p2_init_deck.copy()

    # Play until one player's deck is empty
    while len(p1_deck) > 0 and len(p2_deck) > 0:
        p1_card = p1_deck.popleft()
        p2_card = p2_deck.popleft()

        if p1_card > p2_card:
            # Player 1 wins
            p1_deck.append(p1_card)
            p1_deck.append(p2_card)
        else:
            # Player 2 wins, as all cards are different due to the
            # player decks being drawn from one large deck
            p2_deck.append(p2_card)
            p2_deck.append(p1_card)
        
    if len(p1_deck) > 0:
        winning_deck = p1_deck
    else:
        winning_deck = p2_deck
    
    # Calculate the winning player's score
    score = 0
    for i in range(1, len(winning_deck) + 1):
        score += i * winning_deck.pop()

    return score


# Part 2 Solver
def play_recursive_combat(p1_deck, p2_deck):
    previous_rounds = set()

    playing = True
    while playing:
        # Check if the current card combination existed in a previous
        # round of this game
        if (tuple(p1_deck), tuple(p2_deck)) in previous_rounds:
            # Instant win for player one
            winning_deck = p1_deck
            winning_player = 1
            break

        # Add the current decks to the set of previously seen combinations
        previous_rounds.add((tuple(p1_deck), tuple(p2_deck)))
        
        p1_card = p1_deck.popleft()
        p2_card = p2_deck.popleft()

        if len(p1_deck) >= p1_card and len(p2_deck) >= p2_card:
            # The winner of this round is determined by playing a new
            # game of Recursive Combat
            p1_subdeck = deque()
            p2_subdeck = deque()

            for i in range(p1_card):
                p1_subdeck.append(p1_deck[i])
            
            for i in range(p2_card):
                p2_subdeck.append(p2_deck[i])

            winning_player = play_recursive_combat(p1_subdeck, p2_subdeck)[1]
        else:
            # The winner of this round is determined the usual Combat way
            if p1_card > p2_card:
                # Player 1 wins
                winning_player = 1
            else:
                # Player 2 wins, as all cards are different due to the
                # player decks being drawn from one large deck
                winning_player = 2
        
        # Add cards to the winner's deck
        if winning_player == 1:
            p1_deck.append(p1_card)
            p1_deck.append(p2_card)
        else:
            p2_deck.append(p2_card)
            p2_deck.append(p1_card)

        # Check whether or not the game is over
        if len(p1_deck) <= 0:
            playing = False
            winning_deck = p2_deck
            winning_player = 2            
        elif len(p2_deck) <= 0:
            playing = False
            winning_deck = p1_deck
            winning_player = 1
    
    # Calculate the winning player's score
    score = 0
    for i in range(1, len(winning_deck) + 1):
        score += i * winning_deck.pop()

    return score, winning_player


print('Part 1 Answer:', play_combat())
print('Part 2 Answer:', play_recursive_combat(p1_init_deck.copy(), p2_init_deck.copy())[0])