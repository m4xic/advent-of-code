import re

with open('input', 'r') as f: instructions = f.read()

total = 0

do = True
print(instructions)
while instructions:
    #print(total)
    if do:
        # First check there's not a dont() coming up
        print(instructions[:7])
        if instructions[:7] == "don't()":
            do = False
            continue
        # Then check if there's a valid mul(xxx,yyy) coming up
        else:
            match = re.search(r"mul\([0-9]{1,3},[0-9]{1,3}\)", instructions[:12])
            if match:
                #print(match.group())
                a, b = match.group().replace("mul(","").replace(")","").split(",")
                total += int(a) * int(b)
                #print(match.span())
                instructions = instructions[match.span()[1]:]
                continue
            else:
                instructions = instructions[1:]
                continue

    else:
        # Check if there's a do() coming up
        print(instructions[:4])
        if instructions[:4] == "do()":
            do = True
            continue
        else:
            instructions = instructions[1:]

print(total)