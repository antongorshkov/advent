lines = [s.strip() for s in open('day12.input').readlines()]

def moveShip(x,y,direction,param):
    if   direction == 'N': y += param
    elif direction == 'S': y -= param
    elif direction == 'E': x += param
    elif direction == 'W': x -= param
    return x,y

def pt1():
    x = y = 0
    currentDirection = 'E'
    directions = { 'N' : 0, 'S': 180, 'E': 90, 'W' : 270 }
    degrees = { 0 : 'N', 180 :'S', 90 : 'E', 270 :'W' }
    currentDegrees = 0 + directions[currentDirection]
    for inst in lines:
        action = inst[0]
        param = int(inst[1:])
        if action in 'LR':
            if action == 'R':
                currentDegrees = (currentDegrees + param) % 360
            elif action == 'L':
                currentDegrees = (currentDegrees - param) % 360
            currentDirection = degrees[currentDegrees]
            continue
        if action == 'F':
            direction = currentDirection
        if action in 'NSEW':
            direction = action
        x,y = moveShip(x,y,direction,param)
    return  abs(x) + abs(y)

def pt2():
    x = y = 0
    wayX = 10
    wayY = 1
    degrees = { 'R90'  :lambda x,y: (y,-x),
                'R180' :lambda x,y: (-x,-y),
                'R270' :lambda x,y: (-y,x),
                'L90'  :lambda x,y: (-y,x),
                'L180' :lambda x,y: (-x,-y),
                'L270' :lambda x,y: (y,-x),
    }
    for inst in lines:
        action = inst[0]
        param = int(inst[1:])
        if action in 'LR':
            wayX,wayY = degrees[inst](wayX,wayY)
        elif action == 'F':
            x = x + param * wayX
            y = y + param * wayY
        elif action in 'NSEW':
            wayX,wayY = moveShip(wayX,wayY,action,param)

    return  abs(x) + abs(y)

print pt1()
print pt2()
