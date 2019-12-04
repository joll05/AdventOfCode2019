
def CheckPossibility(num):
    digits = [int(d) for d in str(num)]

    lastDigit = 0
    hasConsecutive = False
    for i in digits:
        if(lastDigit > i):
            return False
        if(lastDigit == i):
            hasConsecutive = True
        
        lastDigit = i
    else:
        if(hasConsecutive == False):
            return False
    
    return True

Min = 248345
Max = 746315

total = 0

# There is definitely a better way of doing this, but I'm just going to test every possible combination

for d in range(Min, Max + 1):
    if(CheckPossibility(d) == True):
        total+=1

print(total)
