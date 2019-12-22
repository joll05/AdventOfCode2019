deckSize = 10007

def NewStack(deck):
    return list(reversed(deck))

def Cut(deck, N):
    return deck[N:] + deck[:N]

def DealWithIncrement(deck, N):
    size = len(deck)
    newDeck = [None] * size
    
    for i, card in enumerate(deck):
        pos = i * N % size
        # Note: if 'deal with increment' could use negative numbers this would not work. In this case, it can't.
        newDeck[pos] = card

    return newDeck

f = open("input.txt", "r")

instructions = f.readlines()

myDeck = list(range(deckSize))

for i in instructions:
    if(i.startswith("deal into new stack")):
        myDeck = NewStack(myDeck)
    elif(i.startswith("cut")):
        myDeck = Cut(myDeck, int(i[4:]))
    elif(i.startswith("deal with increment")):
        myDeck = DealWithIncrement(myDeck, int(i[20:]))
    else:
        raise Exception("Invalid instruction")

resultFile = open("output.txt", "w")
resultFile.write(str(myDeck))

print("Card 2029 is at position", myDeck.index(2019))
print("The whole deck is written at output.txt")
