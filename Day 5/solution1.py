import inspect

f = open("input.txt", "r")

values = f.read().split(",")

def opcode1(p1, p2, out):
    values[out] = str(p1 + p2)
def opcode2(p1, p2, out):
    values[out] = str(p1 * p2)
def opcode3(out):
    values[out] = input("Input required: ")
def opcode4(p1):
    print(p1)
def opcode99():
    exit()

pointer = 0

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

    eval(func + "(%s)" % args)
    pointer += len(params) + 1
            
