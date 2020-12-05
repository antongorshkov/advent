from string import maketrans

def getSid(row,col): return row * 8 + col
def decodePass(input):
    table = maketrans('FBLR', '0101')
    input = input.translate(table)
    row = int(input[0:7],2)
    col = int(input[7:10],2)
    return [row,col]

def find_missing(lst):
    return sorted(set(range(lst[0], lst[-1] + 1)).difference(lst))

allSids = []
with open('day5.input') as inputFile:
    for line in inputFile:
        [row,col] = decodePass(line)
        allSids.append(getSid(row,col))

print max(allSids)
print find_missing(allSids)
