from string import maketrans

def decodePass(input):
    table = maketrans('FBLR', '0101')
    return int(input.translate(table),2)

allSids = []
with open('day5.input') as inputFile:
    for line in inputFile:
        allSids.append(decodePass(line))

print max(allSids)
print set(range(min(allSids),max(allSids)))-set(allSids)
