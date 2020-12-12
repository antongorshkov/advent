import copy
instructionsRaw = [list(x.replace('L','2')) for x in open('day11.input', 'r').read().strip().replace('.','0').split('\n')]

instructions = []
for inst in instructionsRaw:
    instructions.append(map(lambda x: int(x)-1, inst))

''' At this point we have array of arrays where 1 represents occuipied seat and -1 represents floor '''

def isOccupied(seat,seating):
    x = seat[0]
    y = seat[1]
    val = 0
    if 0 <= x < len(seating) and 0 <= y < len(seating[x]) and seating[x][y] >= 0:
        val = seating[x][y]
    return val

def inRange(x,y,seating):
    return 0 <= x < len(seating) and 0 <= y < len(seating[x])

def countAdjacent2(x,y,seating):
    directions = {
    'S':  [1,0],
    'SW' :[1,-1],
    'SE' :[1,1],
    'W' : [0,-1],
    'E' : [0,1],
    'N' : [-1,0],
    'NW': [-1,-1],
    'NE': [-1,1]
    }
    counter = 0
    for dir in directions:
        currX = x
        currY = y
        while(True):
            currX += directions[dir][0]
            currY += directions[dir][1]
            if not inRange(currX,currY,seating): break
            if seating[currX][currY] < 0: continue
            counter += seating[currX][currY]
            break
    return counter


'''Given a seat, calculated number of seats next to it that are occupied'''
def countAdjacent(x,y,seating):
    adjacentSeats = [[x+1,y],[x+1,y+1],[x,y+1],[x-1,y+1],[x-1,y],[x-1,y-1],[x,y-1],[x+1,y-1]]
    counter = 0
    for seat in adjacentSeats:
        counter += isOccupied(seat,seating)
    return counter

def printInst(seating):
    s = ''
    newInst = copy.deepcopy(seating)
    for x, inst in enumerate(instructions):
        for y, seat in enumerate(inst):
            if seat == 1:
                newInst[x][y] = '#'
            elif seat == 0:
                newInst[x][y] = 'L'
            elif seat == -1:
                newInst[x][y] = '.'
            else:
                print 'noooooooo we went inside a matrix!!!!!!'

    for x, inst in enumerate(newInst):
        print s.join(inst)

def pt1(seating):
    newInst = copy.deepcopy(seating)
    hasChanged = False
    for x, inst in enumerate(seating):
        for y, seat in enumerate(inst):
            if seat == -1: continue
            adjacentSeatCount = countAdjacent2(x,y,seating)
            if seat == 1 and adjacentSeatCount >= 5:
                newInst[x][y] = 0
                hasChanged = True
            elif seat == 0 and adjacentSeatCount == 0:
                newInst[x][y] = 1
                hasChanged = True

    return(hasChanged,newInst)


while(True):
     hasChanged, instructions = pt1(instructions)
     if not hasChanged: break
     continue

occupiedSeats = 0
for inst in instructions:
    for seat in inst:
        if seat < 0: continue
        occupiedSeats += seat

print occupiedSeats
