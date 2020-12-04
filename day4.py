import re

lines = []
with open('day4.input') as inputFile:
    res = inputFile.read()

passportsRaw = res.split("\n\n")

requiredFields = {'byr','iyr','eyr','hgt','hcl','ecl','pid'}
def validateByr(x): return int(x) in range(1920,2003)
def validateIyr(x): return int(x) in range(2010,2021)
def validateEyr(x): return int(x) in range(2020,2031)
def validateEcl(x): return x in {'amb','blu','brn','gry','grn','hzl','oth'}
def validatePid(x): return x.isdigit() and len(x) == 9
def validateHcl(x): return re.match(r"#[0-9a-f]{6}", x) is not None
def validateHgt(x): return (("cm" in x and (150 <= int(x.replace("cm", "")) <= 193)) or ("in" in x and (59 <= int(x.replace("in", "")) <= 76)))



passports = []
isValidCnt = 0
for passport in passportsRaw:
    fields = passport.split()
    p = {}
    for field in fields:
        [k,v] = field.split(':')
        p[k]=v
    p.pop('cid', None)
    if (len(requiredFields.difference(p.keys())) == 0
        and validateByr(p['byr'])
        and validateIyr(p['iyr'])
        and validateEyr(p['eyr'])
        and validateHgt(p['hgt'])
        and validateHcl(p['hcl'])
        and validateEcl(p['ecl'])
        and validatePid(p['pid'])
    ):
        isValidCnt += 1
    passports.append(p)

print isValidCnt
