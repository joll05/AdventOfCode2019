import inspect

f = open("input.txt", "r")

values = f.read().split(",")

pointer = 0

finished = False

outfunc = None
infunc = None

def opcode1(p1, p2, out):
    values[out] = str(p1 + p2)
    return True
def opcode2(p1, p2, out):
    values[out] = str(p1 * p2)
    return True
def opcode3(out):
    if(infunc != None):
        values[out] = str(infunc())
    else:
        values[out] = input("Input required: ")
    return True
def opcode4(p1):
    if(outfunc != None):
        outfunc(p1)
    else:
        print(p1)
    return True
def opcode5(p1, p2):
    if(p1 != 0):
        global pointer
        pointer = p2
        return False
    return True
def opcode6(p1, p2):
    if(p1 == 0):
        global pointer
        pointer = p2
        return False
    return True
def opcode7(p1, p2, out):
    if(p1 < p2):
        values[out] = "1"
    else:
        values[out] = "0"
    return True
def opcode8(p1, p2, out):
    if(p1 == p2):
        values[out] = "1"
    else:
        values[out] = "0"
    return True
def opcode99():
    global finished
    finished = True
    return False

def Run(outputfunc=None, inputfunc=None):
    global outfunc
    global infunc
    global pointer
    global values
    global finished
    
    f = open("input.txt", "r")

    values = f.read().split(",")

    pointer = 0

    finished = False

    outfunc = outputfunc
    infunc = inputfunc
    
    while True:
        opcode = int(values[pointer][-2:])
        func = "opcode%d" % opcode
        modes = list(reversed(values[pointer][:-2]))
        params = inspect.getfullargspec(eval(func))[0]
        args = ""
        
        for i in range(len(params)):
            currentValue = values[pointer + 1 + i]
            mode = 0

            if(params[i] != "out"):
                try:
                    mode = int(modes[i])
                except IndexError:
                    pass
            else:
                mode = 1
                    
            if(i != 0):
                args += ","

            if(mode == 0):
                args += values[int(currentValue)]
            elif(mode == 1):
                args += currentValue

        if(eval(func + "(%s)" % args)):
            pointer += len(params) + 1

        if(finished):
            return

Run(None, None)
