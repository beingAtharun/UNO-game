import random
# Creating UNO Deck of 108 cards
def Deck():
    deck = []
    values = [0,1,2,3,4,5,6,7,8,9,'skip','Reverse','Draw Two']
    colours = ['Red','Yellow','Blue','Green']
    extra_cards = ['Wild','Wild Draw Four']
    for i in colours:
        for j in values:
            card_value = "{} {}".format(i,j)
            deck.append(card_value)
            if j != 0:
                deck.append(card_value)
    for k in range(4):
        for p in range(2):
            deck.append(extra_cards[p])
    return deck
# Shuffling the deck of cards
def shuffled_deck(deck):
    for card_position in range(len(deck)):
        random_position = random.randint(0,107)
        deck[card_position],deck[random_position] = deck[random_position],deck[card_position]
    return deck
# To Draw the cards from the deck of card
def draw_cards(no_of_cards):
    drawed_cards = []
    for i in range(no_of_cards):
        drawed_cards.append(x.pop(0))
    return drawed_cards
#To show the cards that are with the player 
def show_cards(player_cards, cards_with_player):
    if player_cards <0 or player_cards >no_of_players:
        print("player {}".format(player_cards+no_of_players+1))
    else:
        print("player {}".format(player_cards+1))
    print("Cards in your Hand \n")
    y = 1
    for i in cards_with_player:
        print("{}. {}".format(y,i))
        y+=1
    print("")
#Check whether a player can play or not
def can_play(colour, value, cards_with_player):
    for i in cards_with_player:
        if "Wild" in i:
            return True
        elif colour in i or value in i:
            return True
    return False
x = Deck()
x = shuffled_deck(x)
discard_card = []
player_cards = []
print(player_cards)
colours = ['Red','Yellow','Blue','Green']
no_of_players = int(input("\nEnter player count ?\n"))
while (no_of_players<2 or no_of_players>10):
    no_of_players = int(input("\nInvalid. Please the enter the count in between 2 - 10. Enter player count?\n"))
for i in range(no_of_players):
    player_cards.append(draw_cards(7))
player_turn = 0
player_direction = 1
playing = True 
discard_card.append(x.pop(0))
splitcard = discard_card[0].split(" ",1)
current_colour = splitcard[0]
if current_colour != "Wild":
    card_value = splitcard[1]
else:
    card_value = "Any"
while playing:
    show_cards(player_turn,player_cards[player_turn])
    print("card on top of discard pile: {}".format(discard_card[-1]))
    if can_play(current_colour, card_value, player_cards[player_turn]):
        card_choosen = int(input("Which card do you want to choose?"))
        while not can_play(current_colour, card_value, [player_cards[player_turn][card_choosen-1]]):
            card_choosen = int(input("Invalid. Please enter the card you want to choose. Which card do you want to choose?"))
        print("you played {}".format(player_cards[player_turn][card_choosen-1]))
        discard_card.append(player_cards[player_turn].pop(card_choosen-1))
        #Winning condition
        if len(player_cards[player_turn]) == 1:
            playing = False
            winner = " \n \n Winner is Player {} !".format(player_turn+1)
            print(winner)
        else:
            #Functionality of special cards
            splitcard = discard_card[-1].split(" ",1)
            current_colour = splitcard[0]
            if len(splitcard) == 1 :
                card_value = "Any"
            else:
                card_value = splitcard[1]
            if current_colour == 'Wild':
                for i in range(len(colours)):
                    print("{}.{}".format(i+1,colours[i]))
                new_colour = int(input("Enter the colour that you want to choose:\n"))
                while new_colour <1 or new_colour>4:
                    new_colour = int(input("Invalid colour.Enter the colour that you want to choose:\n"))
                current_colour = colours[new_colour-1]
            if card_value == 'Reverse':
                player_direction = player_direction * -1
            elif card_value == 'skip':
                player_turn += player_direction
                if player_turn >= no_of_players:
                    player_turn = 0
                elif player_turn < 0:
                    player_turn = no_of_players-1
            elif card_value == 'Draw Two':
                player_draw = player_turn + player_direction
                if player_draw == no_of_players:
                    player_draw = 0
                elif player_draw < 0:
                    player_draw == no_of_players-1
                player_cards[player_draw].extend(draw_cards(2))
            elif card_value == 'Draw Four':
                player_draw = player_turn + player_direction
                if player_draw == no_of_players:
                    player_draw = 0
                elif player_draw < 0:
                    player_draw == no_of_players-1
                player_cards[player_draw].extend(draw_cards(4))
            print("")

    else:
        print("You can't play. You should draw a card.")
        player_cards[player_turn].extend(draw_cards(1))
    player_turn += player_direction
    if player_turn >= no_of_players:
        player_turn = 0
    elif player_turn < 0:
        player_turn == no_of_players-1
