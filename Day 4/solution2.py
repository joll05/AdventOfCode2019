def CheckConsecutive(index, digits):
    currentIndex = index - 1
    sequence = [False, True, True, False]

    for i in sequence:
        #print((digits[currentIndex] != digits[index]) != i)
        if((digits[currentIndex] == digits[index]) != i):
            return False
        currentIndex += 1

    return True

def CheckPossibility(num):
    digits = [int(d) for d in str(num)] + [-1] * 5

    hasConsecutive = False
    for i in range(len(digits) - 5):
        if(digits[i - 1] > digits[i]):
            return False
        if(not hasConsecutive):
            hasConsecutive = CheckConsecutive(i, digits)
    else:
        if(not hasConsecutive):
            return False

    return True

# Inputs
Min = 248345
Max = 746315

total = 0

# There is definitely a better way of doing this, but I'm just going to test every possible combination

for d in range(Min, Max + 1):
    if(CheckPossibility(d)):
        total+=1

print(total)
