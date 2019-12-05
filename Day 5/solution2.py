import inspect

f = open("input.txt", "r")

values = f.read().split(",")

pointer = 0

def opcode1(p1, p2, out):
    values[out] = str(p1 + p2)
    return pointer + 4
def opcode2(p1, p2, out):
    values[out] = str(p1 * p2)
    return pointer + 4
def opcode3(out):
    values[out] = input("Input required: ")
    return pointer + 2
def opcode4(p1):
    print(p1)
    return pointer + 2
def opcode5(p1, p2):
    if(p1 != 0):
        return p2
    return pointer + 3
def opcode6(p1, p2):
    if(p1 == 0):
        return p2
    return pointer + 3
def opcode7(p1, p2, out):
    if(p1 < p2):
        values[out] = "1"
    else:
        values[out] = "0"
    return pointer + 4
def opcode8(p1, p2, out):
    if(p1 == p2):
        values[out] = "1"
    else:
        values[out] = "0"
    return pointer + 4
def opcode99():
    exit()

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

    pointer = eval(func + "(%s)" % args)
            
