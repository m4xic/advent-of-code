import re

with open("input3", "r") as f:
    lines = f.readlines()

total = 0

for line in lines:
    line = line.strip()
    # print(line)
    split = re.split(r"[a-zA-Z]+", line)
    # print(split)
    rejoin = "".join(split)
    # print(rejoin)
    calibration = rejoin[0] + rejoin[-1]
    # print(calibration)
    total += int(calibration)

print(total)
