#card = ["SA", "SK", "SQ", "SJ", "S10", "S9", "S8", "S7", "S6", "S5", "S4", "S3", "S2",
# "HK", "HQ", "HJ", "H10", "H9", "H8", "H7", "H6", "H5", "H4", "H3", "H2",
# "CK", "CQ", "CJ", "C10", "C9", "C8", "C7", "C6", "C5", "C4", "C3", "C2",
# "DK", "DQ", "DJ", "D10", "D9", "D8", "D7", "D6", "D5", "D4", "D3", "D2"]
#Format to print string and number: print("abcd " + str(5))
import random
type = ["S", "H", "C", "D"]
rank = ["A", "K", "Q", "J", "10", "9", "8", "7", "6", "5", "4", "3", "2"]
deck = []

def newDeck():
    for i in range(len(type)):
        for j in range(len(rank)):
            deck.append(type[i] + rank[j] )

    #print(deck)
    random.shuffle(deck)
    return(deck)

#print(newDeck())

#def game(deck):
#   x = input("choose a card =")
#   y = deck[x]
#   return(y)
unpaired=26
z=newDeck()

while unpaired>0:
    print(z)
    x = int(input("choose 1st card ="))
    card1 = z[(x-1)] #String
    print(card1)
    card1Value = card1[-1:]
    print(card1Value)
    y = int(input("choose 2nd card ="))
    card2 = z[(y-1)] #String
    print(card2)
    card2Value = card2[-1:]
    print(card2Value)

    if (card1!='') and (card2!='') and (card1Value==card2Value):
        print("card match")
        z[(x-1)]=""
        z[(y-1)]=""
        unpaired=unpaired-1

    #print(z)
    print(str(unpaired) + " still unpaired. Keep going.")
print('All paired. End game. Thanks for playing')

#list(dict.values()) to get the rank2

#x = int(input("choose 1st card ="))
#card1 = z[(x-1)] #String
#if card1=='':
#    print('card selected. try again')
#else:
#    print(card1)
#    card1Value = card1[-1:]
#    print(card1Value)
#y = int(input("choose 2nd card ="))
#card2 = z[(y-1)] #String
#print(card2)
#card2Value = card2[-1:]
#print(card2Value)
