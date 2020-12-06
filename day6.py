groupInputs = open("day6.input", "r").read().split("\n\n")
def pt1():
    total = 0
    for gInput in groupInputs:
        gInput = gInput.replace('\n','')
        total += len(set(gInput))
    return total

def pt2():
    total = 0
    for line in groupInputs:
        lines = [set(line) for line in line.strip().split("\n")]
        total += len(reduce(lambda x, y: x & y, lines))
    return total
print pt1()
print pt2()
