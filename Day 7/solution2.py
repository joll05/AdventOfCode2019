import computer
import itertools

possibleOrders = list(itertools.permutations(range(5)))

inputs = [0, 0]

bestResult = 0

def RecieveOutput(output):
    global inputs

    inputs[1] = output

index = 0
def SendInput():
    global index
    index += 1
    return(inputs[(index - 1) % len(inputs)])

for i in possibleOrders:
    inputs = [0, 0]
    index = 0
    for j in i:
        inputs[0] = j
        
        computer.Run(RecieveOutput, SendInput)

    result = inputs[1]

    if(result > bestResult):
        bestResult = result

print(bestResult)
