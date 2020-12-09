instructions = [x.split(' ') for x in open('day8.input', 'r').read().strip().split('\n')]
# instructions = [x.split(' ') for x in open('day8.sample', 'r').read().strip().split('\n')]

nodes = {}
i = 0
while i < len(instructions):
    if instructions[i][0] == 'acc':
        nodes[i + 1] = i
    elif instructions[i][0] == 'jmp':
        nodes[i + int( instructions[i][1] )] = i
    else:
        nodes[i + 1] = i
    i += 1

# print nodes

def pt1():
    visited = set()
    i = 0
    acc = 0
    while i < len(instructions):
        #if i == 640: print 'visited 640!!!'
        if i in visited:
            print visited
            print len(visited)
            return acc
        visited.add(i)
        if instructions[i][0] == 'acc':
            acc += int( instructions[i][1] )
        elif instructions[i][0] == 'jmp':
            i += int( instructions[i][1] )
            continue
        i += 1

def pt2():
    visited = set()
    terminationPath = set()
    i = len(instructions) - 1
    while i > 0:

        if i in terminationPath: break
        terminationPath.add(i)
        if i not in nodes: break
        i = nodes[i]
        print terminationPath
    visited = set()
    i = 0
    acc = 0
    while i < len(instructions):
        if i in visited:
            # print visited
            # print len(visited)
            return acc
        visited.add(i)
        inst = instructions[i][0]
        if inst == 'jmp' and (i+1) in terminationPath:
            print 'jpm change at ', i
            inst = 'nop'
        elif inst == 'nop' and (i+int( instructions[i][1] )) in terminationPath:
            print 'nop change at ', i
            inst = 'jmp'

        if inst == 'acc':
            acc += int( instructions[i][1] )
            i += 1
        elif inst == 'jmp':
            i += int( instructions[i][1] )
        else:
            i += 1
    return acc



#print pt1()
print pt2()
