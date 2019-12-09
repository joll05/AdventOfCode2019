import inspect
import sys

def Run(outputfunc=None, inputfunc=None):

    f = open("input.txt", "r")

    values = f.read().split(",")

    values += ["0"] * 9999

    pointer = 0

    relativeBase = 0

    finished = False

    outfunc = outputfunc
    infunc = inputfunc

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
            nonlocal pointer
            pointer = p2
            return False
        return True
    def opcode6(p1, p2):
        if(p1 == 0):
            nonlocal pointer
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
    def opcode9(p1):
        nonlocal relativeBase
        relativeBase += p1
        return True
    def opcode99():
        nonlocal finished
        finished = True
        return False

    while True:
        opcode = int(values[pointer][-2:])
        func = "opcode%d" % opcode
        modes = list(reversed(values[pointer][:-2]))
        params = inspect.getfullargspec(eval(func))[0]
        args = ""
        
        for i in range(len(params)):
            currentValue = values[pointer + 1 + i]
            mode = 0

            try:
                mode = int(modes[i])
            except IndexError:
                pass
                    
            if(i != 0):
                args += ","
            if(params[i] == "out"):
                if(mode == 0):
                    args += currentValue
                elif(mode == 1):
                    raise Exception("An outputs parameter mode can't be of type immediate mode.")
                elif(mode == 2):
                    args += str(relativeBase + int(currentValue))
            else:
                if(mode == 0):
                    args += values[int(currentValue)]
                elif(mode == 1):
                    args += currentValue
                elif(mode == 2):
                    args += values[relativeBase + int(currentValue)]

        if(eval(func + "(%s)" % args)):
            pointer += len(params) + 1

        if(finished):
            return

args = sys.argv
args.pop(0)

for arg in args:
    if(arg == "--run"):
        Run()
