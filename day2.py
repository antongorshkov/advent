isValid = 0
with open('day2.input') as inputFile:
    for line in inputFile:
        rule, char, pw = line.split()
        char = char[0]
        minOccur, maxOccur = [int(x) for x in rule.split('-')]
        charCount = pw.count(char)
        pos1 = pw[minOccur-1] == char
        pos2 = pw[maxOccur-1] == char
        if (pos1 and not pos2) or (not pos1 and pos2):
            isValid +=1
        #if minOccur <= charCount <= maxOccur:
        #    isValid += 1

print isValid
