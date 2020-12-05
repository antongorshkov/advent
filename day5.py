def getSid(row,col): return row * 8 + col
def decodePass(input):
    for letter, number in {'F':'0','B':'1','R':'1','L':'0'}.items():
        input = input.replace(letter, number)
    row = int(input[0:7],2)
    col = int(input[7:10],2)
    return [row,col]

def find_missing(lst):
    start = lst[0]
    end = lst[-1]
    return sorted(set(range(start, end + 1)).difference(lst))

allSids = []
with open('day5.input') as inputFile:
    for line in inputFile:
        [row,col] = decodePass(line)
        allSids.append(getSid(row,col))

print max(allSids)
print find_missing(allSids)
