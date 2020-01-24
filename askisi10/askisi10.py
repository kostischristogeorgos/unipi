#This is the 10th exercise for the first semester class introduction to programming in UniPi
#This program simulates a poker game between two players, in this instance a player and the computer
#First it gives the players 5 cards and it computes which player wins based on the rules and prints out the data
#This program covers the rules from HighestHand to Flush because only 6 rules where asked to be done
#In the future the other 4 rules might be covered as well

import random
suits = ['H', 'D', 'S', 'C']
numbers = []
deck = []
#Makes a list with numbers from 2-14
for i in range(0, 13):
    numbers.append(i+2)
#Makes a two dimensional list with numebers and suits
for i in range(len(suits)):
    for j in range(len(numbers)):
        deck.append([numbers[j], suits[i]])
player1 = []
pc = []
#Shuffles the deck
random.shuffle(deck)
#Puts the random cards in two lists, player1's and pc's list is equal to their respective cards
for i in range(5):
    player1.append(deck.pop())
    pc.append(deck.pop())
#Prints the current cards
print("player1:")
for i in range(5):
        if player1[i][0] == 11:
            print("[ J", ",", player1[i][1], "]", end =" ")
        elif player1[i][0] == 12:
            print("[ Q"," ,", player1[i][1], "]", end =" ")
        elif player1[i][0] == 13:
            print("[ K", ",", player1[i][1], "]", end =" ")
        elif player1[i][0] == 14:
            print("[ A", ",", player1[i][1], "]", end =" ")
        else:
            print("[", player1[i][0], ",", player1[i][1], "]", end =" ")
print("\n")
print("\nPC:",)
for i in range(5):
    if pc[i][0] == 11:
        print("[ J", ",", pc[i][1], "]", end =" ")
    elif pc[i][0] == 12:
        print("[ Q", ",", pc[i][1], "]", end =" ")
    elif pc[i][0] == 13:
        print("[ K", ",", pc[i][1], "]", end =" ")
    elif pc[i][0] == 14:
        print("[ A", ",", pc[i][1], "]", end =" ")
    else:
        print("[", pc[i][0], ",", pc[i][1], "]", end =" ")

#Functions that checks who has the highest card
def Highesthand(player,computer):
    #Sorts the lists
    player = (sorted(player, key=lambda x: x[0], reverse=True))
    computer = (sorted(computer, key=lambda x: x[0], reverse=True))
    max = 0
    user =  "player1"
    logic = False
    #Finds the highest card
    for i in range(5):
        if player[i][0] > computer[i][0]:
            max = player[i][0]
            logic = True
            return logic, max, user
        elif player[i][0] < computer[i][0]:
            max = computer[i][0]
            logic = True
            user = "PC"
            return logic, max, user
        else:
            continue
    else:
        print("Deck is the same, there's no winner")
    return logic, max, user



def Pair(player,computer):
    player = (sorted(player, key=lambda x: x[0], reverse=True))
    computer = (sorted(computer, key=lambda x: x[0], reverse=True))
    max1 = 0
    max2 = 0
    logic = False
    user = "player1"
    #Checks for a double pair in both lists
    for i in range(4):
        if player[i][0] == player[i+1][0]:
            max1 = player[i][0]
            break
    for i in range(4):
        if computer[i][0] == computer[i+1][0]:
            max2 = computer[i][0]
            break
    # if a pair has been found it sends the data back
    if max1 != 0 or max2 != 0:
        if max1 > max2:
            logic = True
            return logic, max1, user
        elif max1 < max2:
            logic = True
            user = "PC"
            return logic, max2, user
        else: #If the largest card is the same in both lists
            for i in range(5):
                if player[i][0] > computer[i][0]:
                    logic = True
                    return logic, max1, user
                elif player[i][0] < computer[i][0]:
                    logic = True
                    user = "PC"
                    return logic, max2, user
                else:
                    continue
            else:
                print("Deck is the same but based on the next rule")
                return logic, 0, 0
    else:
        return logic, 0, 0


def DoublePair(player,computer):
    player = (sorted(player, key=lambda x: x[0], reverse=True))
    computer = (sorted(computer, key=lambda x: x[0], reverse=True))
    max1 = 0
    max2 = 0
    max3 = 0
    max4 = 0
    logic = False
    user = "player1"
    #Checks for 2 double pairs
    for i in range(2):
        if player[i][0] == player[i+1][0] and player[i+2][0] == player[i+3][0]:
            max1 = player[i][0]
            max2 = player[i+2][0]
            break
    for i in range(2):
        if computer[i][0] == computer[i+1][0] and computer[i+2][0] == computer[i+3][0]:
            max3 = computer[i][0]
            max4 = computer[i+2][0]
            break
    if max1 != 0 or max2 != 0:
        if max1 > max3:
            logic = True
            return logic ,max1, max2, user
        elif max1 < max3:
            logic = True
            user = "PC"
            return logic, max3, max4, user
        else:
            for i in range(5):
                if player[i][0] > computer[i][0]:
                    logic = True
                    return logic, max1, max2, user
                elif player[i][0] < computer[i][0]:
                    logic = True
                    user = "PC"
                    return logic, max3, max4, user
                else:
                    continue
            else:
                print("Deck is the same but based on the next rule")
                return logic, 0, 0, 0
    else:
        return logic, 0, 0, 0


def ThreeOfAKind(player,computer):
    player = (sorted(player, key=lambda x: x[0], reverse=True))
    computer = (sorted(computer, key=lambda x: x[0], reverse=True))
    max1 = 0
    max2 = 0
    logic = False
    user = "player1"
    #Checks for 3 same cards in the lists
    for i in range(3):
        if player[i][0] == player[i+1][0] and player[i+1][0] == player[i+2][0]:
            max1 = player[i][0]
            break
    for i in range(3):
        if computer[i][0] == computer[i+1][0] and computer[i+1][0] == computer[i+2][0]:
            max2 = computer[i][0]
            break

    if max1 != 0 or max2 != 0:
        if max1 > max2:
            logic = True
            return logic, max1, user
        elif max1 < max2:
            user = "PC"
            logic = True
            return logic, max2, user
        else:
            for i in range(5):
                if player[i][0] > computer[i][0]:
                    logic = True
                    return logic, max1, user
                elif player[i][0] < computer[i][0]:
                    logic = True
                    user = "PC"
                    return logic, max2, user
                else:
                    continue
            else:
                print("Deck is the same but based on the next rule")
                return logic, 0, 0

    else:
        return logic, 0, 0

def Straight(player,computer):
    player = (sorted(player, key=lambda x: x[0], reverse=True))
    computer = (sorted(computer, key=lambda x: x[0], reverse=True))
    max = 0
    min = 0
    logic = False
    user = "player1"
    s = 0
    s2 = 0
    #checks for a straight with a counter, if the counter is 4 it means that there's at least one player with a straight
    for i in range(4):
        if player[i][0] - player[i+1][0] == 1:
            s = s + 1
        if computer[i][0] - computer[i+1][0] == 1:
            s2 = s2 + 1
    #sends back the data and checks if the decks have the cards in them
    if s == 4 and s2 < 4:
            logic = True
            max = player[0][0]
            min = player[4][0]
            return logic, max, min, user
    elif s2 == 4 and s < 4:
            logic = True
            user = "PC"
            max = computer[0][0]
            min = computer[4][0]
            return logic, max, min, user
    # if both players have a staight, the highest card wins
    elif s == 4 and s2 ==4:
        for i in range(5):
            if player[i][0] > computer[i][0]:
                logic = True
                max = player[0][0]
                min = player[4][0]
                return logic, max, min, user
            elif player[i][0] < computer[i][0]:
                logic = True
                user = "PC"
                max = computer[0][0]
                min = computer[4][0]
                return logic, max, min, user
            else:
                continue
        else:
            print("Both players tie because their Straight is the same but based on the next rule")
            return logic, 0, 0, 0
    else:
        return logic, 0, 0, 0

def Flush(player,computer):
    player = (sorted(player, key=lambda x: x[0], reverse=True))
    computer = (sorted(computer, key=lambda x: x[0], reverse=True))
    s1 = 0
    s2 = 0
    s3 = 0
    s4 = 0
    s5 = 0
    s6 = 0
    s7 = 0
    s8 = 0
    logic = False
    user = "player1"
    suit = ""
    #Checks which suit has been found 5 times in the decks
    for i in range(5):
        if player[i][1] == 'H':
            s1 = s1 + 1
        elif player[i][1] == 'S':
            s2 = s2 +1
        elif player[i][1] == 'C':
            s3 = s3 + 1
        else:
            s4 = s4 + 1

        if computer[i][1] == "H":
            s5 = s5 + 1
        elif computer[i][1] == "S":
            s6 = s6 + 1
        elif computer[i][1] == "C":
            s7 = s7 + 1
        else:
            s8 = s8 + 1

    if s1 == 5:
        suit = "H"
    elif s2 == 5:
        suit = "S"
    elif s3 == 5:
        suit = "C"
    elif s4 == 5:
        suit = "D"
    if s5 == 5:
        suit = "H"
    elif s6 == 5:
        suit = "S"
    elif s7 == 5:
        suit = "C"
    elif s8 == 5:
        suit = "D"
    #Compares the number of cards in the same suit that have been found in both lists
    #if both players have a suit it decides a winner based on the highest card
    if (s1 == 5 or s2 == 5 or s3 == 5 or s4 == 5) and (s5 == 5 or s6 == 5 or s7 == 5 or s8 == 5):
        logic = True
        for i in range(5):
            if player[i][0] > computer[i][0]:
                    print("\nplayer1 has the highest card in the flush")
                    return logic, suit, user
            elif player[i][0] < computer[i][0]:
                    user = "PC"
                    print("\npc has the highest card in the flush")
                    return logic, suit, user
            else:
                continue
        else:
            print("Deck is the same but based on the next rule")
            return logic, 0, 0
    #Checks if one player has a flush and the other doesn't
    elif s1 == 5 or s2 == 5 or s3 == 5 or s4 == 5:
        logic = True
        return logic, suit, user
    elif s5 == 5 or s6 == 5 or s7 == 5 or s8 == 5:
        logic = True
        user = "PC"
        return logic, suit, user
    else:
        return logic, suit, user

#PRINTING
#If logic variable returned by the functions is TRUE then it means that one rule has been found and it breaks the loop and the program ends
#If logic is FALSE then it calls the next functions(rule in order) until there's no rule left
print("\n")
for i in range(1):
    logic, suit, user = Flush(player1, pc)
    if logic:
        print("\nPlayer:", user, "wins because he has a Flush of:", suit)
        break
    logic, cardmax, cardmin, user = Straight(player1,pc)
    if logic:
        #Because the comparison is done using integers, I make the J-A cards visible this way
        if cardmax == 14:
            cardmax = "A"
        elif cardmax == 13:
            cardmax = "K"
        elif cardmax == 12:
            cardmax = "Q"
        elif cardmax == 11:
            cardmax = "J"
        print("\nPlayer:", user, "wins because he has a Straight from:", cardmin, "to", cardmax)
        break
    logic, card, user = ThreeOfAKind(player1, pc)
    if logic:
        if card == 14:
            card = "A"
        elif card == 13:
            card = "K"
        elif card == 12:
            card = "Q"
        elif card == 11:
            card = "J"
        print("\nPlayer:", user, "wins because he has three kinds  of:", card, "s")
        break
    logic, card, card2, user = DoublePair(player1, pc)
    if logic:
        if card == 14:
            card = "A"
        elif card == 13:
            card = "K"
        elif card == 12:
            card = "Q"
        elif card == 11:
            card = "J"

        if card2 == 14:
            card2 = "A"
        elif card2 == 13:
            card2 = "K"
        elif card2 == 12:
            card2 = "Q"
        elif card2 == 11:
            card2 = "J"
        print("\nPlayer:", user, "wins because he has two kinds  of:", card, "s and two kinds of", card2, "s")
        break
    logic, card, user = Pair(player1, pc)
    if logic:
        if card == 14:
            card = "A"
        elif card == 13:
            card = "K"
        elif card == 12:
            card = "Q"
        elif card == 11:
            card = "J"
        print("\nPlayer:", user, "wins because he has two kinds  of:", card, "s")
        break
    else:
        logic, card, user = Highesthand(player1, pc)
        if logic:
            if card == 14:
                card = "A"
            elif card == 13:
                card = "K"
            elif card == 12:
                card = "Q"
            elif card == 11:
                card = "J"
            print("\nPlayer:", user, "wins because he has the highest card/highest card in a tie:", card)
        else:
            print("No winner")
