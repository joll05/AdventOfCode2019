# There is probably a better way of doing it, but I am just going to
# run through every possible case

for noun in range(0, 100):
    for verb in range(0, 100):
        f = open("input.txt", "r")

        inputs = f.read().split(",")

        # convert to integers
        for i in range(0, len(inputs)):
            inputs[i] = int(inputs[i])

        #overrides
        inputs[1] = noun
        inputs[2] = verb
        
        currentPos = 0
    
        while True:
            opcode = inputs[currentPos]

            if(opcode == 99):
                if(inputs[0] == 19690720):
                    print("Noun = %d | Verb = %d | 100 * Noun + Verb = %d" % (noun, verb, 100 * noun + verb))
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
        
