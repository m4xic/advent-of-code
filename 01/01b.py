with open('input', 'r') as f:
    lines = f.readlines()

left, right = [], []

for line in lines:
    l, r = line.split()
    left.append(int(l))
    right.append(int(r))

right2 = {}
for r_item in right:
    if r_item in right2.keys(): right2[r_item] += 1
    else: right2[r_item] = 1

print(right2)

similarity = 0
for l_item in left:
    if l_item in right2.keys():
        similarity += (l_item * right2[l_item])

print(similarity)