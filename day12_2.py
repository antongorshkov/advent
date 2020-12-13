import math

with open('day12.input') as reader:
    plan = [(line[0],int(line[1:])) for line in reader]

east = 0
north = 0
weast = 10
wnorth = 1

def rotate(x,y,degrees):
    rad = (degrees/90) * (math.pi/2)
    return (
        round(x * math.cos(rad) - y * math.sin(rad)),
        round(x * math.sin(rad) + y * math.cos(rad))
    )

wtranslations = {
    'L': lambda v: (east, north, *rotate(weast,wnorth,v)),
    'R': lambda v: (east, north, *rotate(weast,wnorth,-v)),
    'F': lambda v: (east + weast*v, north + wnorth*v, weast, wnorth),
    'N': lambda v: (east, north, weast, wnorth + v),
    'S': lambda v: (east, north, weast, wnorth - v),
    'E': lambda v: (east, north, weast + v, wnorth),
    'W': lambda v: (east, north, weast - v, wnorth)
}

for move in plan:
    (east,north,weast,wnorth) = wtranslations[move[0]](move[1])

print(abs(north) + abs(east))
