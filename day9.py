data = [int(x) for x in open('day9.input', 'r').read().strip().split('\n')]

def findPair(numbers, target):
    for i, num in enumerate(numbers[:-1]):
        compliment = target - num
        if compliment in numbers[i+1:]:
            return([num, compliment])
    return([])

def pt1(preamble):
    i = preamble
    while i < len(data):
        res = findPair(data[i-preamble:i], data[i])
        if not len(res):
            return data[i]
        i += 1

def pt2(target):
    i = 0
    contSet = []
    while i < len(data):
        contSet.append(data[i])
        if sum(contSet) == target:
            return(min(contSet) + max(contSet))
        elif sum(contSet) < target:
            i += 1
        else:
            i = i - len(contSet) - 1
            contSet = []
pt1Res = pt1(25)
print pt1Res
print pt2(pt1Res)
