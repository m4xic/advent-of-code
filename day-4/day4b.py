import re

f = open('test-input', 'r')
b = f.read()
l = b.replace(" ", "\n").split("\n\n")
valid = 0
for record in l:
    validity = [0,0,0,0,0,0,0]
    passport = {}
    record = record.split("\n")
    for item in record:
        if item == '': continue
        item = item.split(":")
        passport[item[0]] = item[1]
    
    if not set(["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]).issubset(passport.keys()): continue # https://www.geeksforgeeks.org/
    try:
        if int(passport["byr"]) in list(range(1920,2003)): validity[0] = 1
        if int(passport["iyr"]) in list(range(2010,2021)): validity[1] = 1
        if int(passport["eyr"]) in list(range(2020,2031)): validity[2] += 1
        if "in" in passport["hgt"]:
            if int(passport["hgt"].split("in")[0]) in list(range(59,76)): validity[3] = 1
        elif "cm" in passport["hgt"]:
            if int(passport["hgt"].split("cm")[0]) in list(range(150,194)): validity[3] = 1
        else:
            validity[3] = 0
        if re.search("^#(?:[0-9a-fA-F]{3}){1,2}$", passport["hcl"]): validity[4] = 1
        if passport["ecl"] in ["amb","blu","brn","gry","grn","hzl","oth"]: validity[5] = 1
        if len(passport["pid"]) == 9:
            if int(passport["pid"]): validity[6] += 1
    except Exception as e:
        print(record)
        print("one of these failed: " + str(e) + "\n")
        continue

    if validity == [1,1,1,1,1,1,1]: valid += 1
print(valid)