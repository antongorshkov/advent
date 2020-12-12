instructions = [int(x) for x in open('day10.input', 'r').read().strip().split('\n')]
instructions.append(0)
instructions.append(max(instructions) + 3)
instructions.sort()

def pt1():
    res = []
    for i, num in enumerate(instructions[:-1]):
        res.append(instructions[i+1] - instructions[i])
    return res.count(1) * res.count(3)

print pt1() 
