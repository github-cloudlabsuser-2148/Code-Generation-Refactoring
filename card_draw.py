# Intentionally flawed Python program

# importing modules
import itertools, random

# make a deck of cards
deck = list(itertools.product(
    range(1, 14), 
    ['Spade', 'Heart', 'Diamond', 'Club']
))

# shuffle the cards
random.shuffle(deck)

# draw five cards
print("You got:")
card_ranks = {1: "Ace", 11: "Jack", 12: "Queen", 13: "King"}
for i in range(5):
   rank = card_ranks.get(deck[i][0], deck[i][0])
   print(rank, "of", deck[i][1])
