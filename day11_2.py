lines = [list(s.strip()) for s in open('day11.input').readlines()]
lines = { (x,y): cell for x,row in enumerate(lines) for y,cell in enumerate(row) }

def neighbors(loc,queen):
    for dx,dy in [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]:
        nloc = (loc[0]+dx,loc[1]+dy)
        while queen and nloc in floor and floor[nloc] not in 'L#': nloc = (nloc[0]+dx,nloc[1]+dy)
        if nloc in floor and floor[nloc]=='#': yield 1

for part in range(2):
    new_floor = lines.copy()
    floor = None
    while new_floor != floor:
        floor = new_floor.copy()
        for loc in floor:
            n = sum(neighbors(loc,part))
            if floor[loc] == 'L' and n == 0: new_floor[loc] = '#'
            if floor[loc] == '#' and n > (3+part): new_floor[loc] = 'L'
    print part
    x = sum(cell=="#" for cell in floor.values())
    print x
    # print(f'part {part+1}: {}')
