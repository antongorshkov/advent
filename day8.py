instructions = [x.split(' ') for x in open('day8.input', 'r').read().strip().split('\n')]

nodes = {}
i = 0
while i < len(instructions):
    increment = int( instructions[i][1] ) if instructions[i][0] == 'jmp' else 1
    nodes[i] = i + increment
    i += 1

def isTerminal(nodeIndex):
    visited = set()
    while True:
        if nodeIndex in visited: return False
        if nodeIndex == len(nodes) - 1: return True
        visited.add(nodeIndex)
        nodeIndex = nodes[nodeIndex]

def pt1():
    visited = set()
    i = 0
    acc = 0
    while i < len(instructions):
        if i in visited:
            return acc
        visited.add(i)
        if instructions[i][0] == 'acc':
            acc += int( instructions[i][1] )
        elif instructions[i][0] == 'jmp':
            i += int( instructions[i][1] )
            continue
        i += 1

def pt2():
    tNodes = set(filter(isTerminal, nodes.keys()))
    i = 0
    acc = 0
    visited = set()
    switched = False
    while i < len(instructions):
        if i in visited: return acc
        visited.add(i)

        if not switched and instructions[i][0] == 'jmp' and (i + 1) in tNodes:
            instructions[i][0] = 'nop'
            switched = True
        elif not switched and instructions[i][0] == 'nop' and (i + int( instructions[i][1] )) in tNodes:
            print 'found nop'
            instructions[i][0] = 'jmp'
            switched = True

        if instructions[i][0] == 'acc':
            acc += int( instructions[i][1] )
        elif instructions[i][0] == 'jmp':
            i += int( instructions[i][1] )
            continue
        i += 1

    return acc



#print pt1()
print pt2()
# print instructions
