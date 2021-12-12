with open('08', 'r') as f: lines = f.read().splitlines()
print(lines)

# 0:  (6)   abcefg
# 1:  (2)   cf
# 2:  (5)   acdeg
# 3:  (5)   acdfg
# 4:  (4)   bcdf
# 5:  (5)   abdfg
# 6:  (6)   abdefg
# 7:  (3)   acf
# 8:  (7)   abcdefg
# 9:  (6)   abcdfg

segments = {1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: []}

for line in lines:
    output = line.split(' | ')[-1]
    for combo in output.split(' '):
        print(combo)
        segments[len(combo)].append(combo)

print(segments)

for key in segments.keys():
    print(f"{key=} {len(segments[key])}")

print(len(segments[2]) + len(segments[4]) + len(segments[3]) + len(segments[7]))