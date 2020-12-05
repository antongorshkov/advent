from string import maketrans

def decodePass(input):
    table = maketrans('FBLR', '0101')
    input = input.translate(table)
    return int(input,2)

def find_missing(lst):
    return sorted(set(range(lst[0], lst[-1] + 1)).difference(lst))

allSids = []
with open('day5.input') as inputFile:
    for line in inputFile:
        allSids.append(decodePass(line))

print max(allSids)
print find_missing(allSids)
