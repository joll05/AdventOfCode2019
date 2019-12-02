f = open("input.txt", "r")

inputs = f.read().split(",")
#inputs = "1,1,1,4,99,5,6,0,99".split(",")

# convert to integers
for i in range(0, len(inputs)):
    inputs[i] = int(inputs[i])

#overrides
inputs[1] = 12
inputs[2] = 2

currentPos = 0

while True:
    opcode = inputs[currentPos]

    if(opcode == 99):
        print(inputs)
        break
    
    arg1 = inputs[inputs[currentPos + 1]]
    arg2 = inputs[inputs[currentPos + 2]]
    out = inputs[currentPos + 3]

    if(opcode == 1):
        result = arg1 + arg2
        inputs[out] = result
    elif(opcode == 2):
        result = arg1 * arg2
        inputs[out] = result
    else:
        print("Something went wrong...")
        break
    
    currentPos += 4
        
