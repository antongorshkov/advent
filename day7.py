import re
data = open('day7.input', 'r').read().strip().split('\n')
rules = {}
rules2 = {}
for r in data:
    r = r.replace('bags','').replace('bag','').replace('  ',' ').replace('.','').replace('no other','0 other')
    [k,v] = r.split('contain')
    val1 = [[int(x.strip()[0]),x[2:].strip()] for x in v.strip().split(',')]
    rules[k.strip()] = val1
    val2 = set(x[2:].strip() for x in v.strip().split(','))
    rules2[k.strip()] = val2

def pt2(counter, bagColor):
    if bagColor not in rules: return 0
    for pairs in rules[bagColor]:
        counter += pairs[0] * pt2(1,pairs[1])
    return counter

def pt1(counter, bagColor, countedBags):
    for item in rules2:
        if bagColor in rules2[item] and item not in countedBags:
            counter += 1
            countedBags.add(item)
            counter += pt1(0,item,countedBags)

    return counter

print pt1(0,'shiny gold',set())
print pt2(0,'shiny gold')
