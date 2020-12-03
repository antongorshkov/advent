from functools import reduce
lines = []
with open('day3.input') as inputFile:
    for line in inputFile:
        line = line.rstrip("\n")
        lines.append(list(line))

pairs = [ [1,1],[3,1],[5,1],[7,1],[1,2] ]
res = []
for pair in pairs:
    [x,y] = pair
    xPos = yPos = 0
    trees = 0
    while yPos < len(lines) - 1:
        yPos += y
        xPos += x
        line = lines[yPos]
        if xPos >= len(line):
            xPos = xPos - len(line)
        if line[xPos] == "#":
            trees += 1
    res.append(trees)
print reduce(lambda x, y: x*y, res)
