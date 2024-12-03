import re

with open('input', 'r') as f: instructions = f.read()

results = re.findall(r"mul\([0-9]{1,3},[0-9]{1,3}\)", instructions)

total = 0
for result in results:
    a, b = result.replace("mul(","").replace(")","").split(",")
    print(f"{result=} {a=} {b=} {int(a) * int(b)=}")
    total += int(a) * int(b)

print(total)