import re

requiredFields = {'byr','iyr','eyr','hgt','hcl','ecl','pid'}
def validateByr(x): return int(x) in range(1920,2003)
def validateIyr(x): return int(x) in range(2010,2021)
def validateEyr(x): return int(x) in range(2020,2031)
def validateEcl(x): return x in {'amb','blu','brn','gry','grn','hzl','oth'}
def validatePid(x): return x.isdigit() and len(x) == 9
def validateHcl(x): return re.match(r"#[0-9a-f]{6}", x) is not None
def validateHgt(x): return (("cm" in x and (150 <= int(x.replace("cm", "")) <= 193)) or ("in" in x and (59 <= int(x.replace("in", "")) <= 76)))
def isAllFields(x): return len(requiredFields.difference(x)) == 0

lines = []
passportsRaw = open("day4.input", "r").read().split("\n\n")

isValidCnt = 0
for passport in passportsRaw:
    p = {f.split(':')[0]:f.split(':')[1] for f in passport.split()}
    isValidCnt += 1 if (
            isAllFields(p.keys())
        and validateByr(p['byr'])
        and validateIyr(p['iyr'])
        and validateEyr(p['eyr'])
        and validateHgt(p['hgt'])
        and validateHcl(p['hcl'])
        and validateEcl(p['ecl'])
        and validatePid(p['pid'])
    ) else 0


print isValidCnt
