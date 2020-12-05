f = open('input', 'r')
b = f.read()
l = b.replace(" ", "\n").split("\n\n")
valid = 0
for record in l:
    passport = {}
    record = record.split("\n")
    for item in record:
        if item == '': continue
        item = item.split(":")
        passport[item[0]] = item[1]
    if set(["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]).issubset(passport.keys()): valid += 1 # https://www.geeksforgeeks.org/python-check-if-one-list-is-subset-of-other/
print(valid)