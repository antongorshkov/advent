groupInputs = open("day6.input", "r").read().split("\n\n")
def pt1():
    total = 0
    for gInput in groupInputs:
        gInput = gInput.replace('\n','')
        total += len(set(gInput))
    print total

def pt2():
    total = 0
    allLines = []
    for gInput in groupInputs:
        lines = [line for line in gInput.split('\n') if line.strip() != '']
        total += len(reduce(lambda x, y: set(x).intersection(set(y)), lines))
        allLines.append(lines)
    print total
pt1()
pt2()
