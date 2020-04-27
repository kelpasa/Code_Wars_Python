'''
Steve and Josh are bored and want to play something. They don't want to think too much, so they come up with a really simple game. Write a function called winner and figure out who is going to win.

They are dealt the same number of cards. They both flip the card on the top of their deck. Whoever has a card with higher value wins the round and gets one point (if the cards are of the same value, neither of them gets a point). After this, the two cards are discarded and they flip another card from the top of their deck. They do this until they have no cards left.

deckSteve and deckJosh are arrays representing their decks. They are filled with cards, represented by a single character. The card rank is as follows (from lowest to highest):

'2','3','4','5','6','7','8','9','T','J','Q','K','A'
Every card may appear in the deck more than once. Figure out who is going to win and return who wins and with what score:

"Steve wins x to y" if Steve wins; where x is Steve's score, y is Josh's score;
"Josh wins x to y" if Josh wins; where x is Josh's score, y is Steve's score;
"Tie" if the score is tied at the end of the game.'''

def winner(deck_steve, deck_josh):
    contener ={
        '2':2,
        '3':3,
        '4':4,
        '5':5,
        '6':6,
        '7':7,
        '8':8,
        '9':9,
        'T':10,
        'J':11,
        'Q':12,
        'K':13,
        'A':14
    }
    arr_steve = []
    arr_josh = []
    for i in deck_josh:
        arr_josh.append(contener[i])
    for i in deck_steve:
        arr_steve.append(contener[i])

    steve = 0
    josh = 0


    for s, j in zip(arr_steve,arr_josh):
        if s > j:
            steve +=1
        elif s < j:
            josh += 1
        elif s == j:
            steve +=0
            josh +=0

    if steve > josh:
        return f'Steve wins {steve} to {josh}'
    elif steve < josh:
        return  f'Josh wins {josh} to {steve}'
    else:
        return "Tie"
