with open('input', 'r') as f:
    lines = f.readlines()

left, right = [], []

for line in lines:
    l, r = line.split()
    left.append(int(l))
    right.append(int(r))

left.sort()
right.sort()

if len(left) != len(right): print('fail')
else:
    diff = 0
    for i in range(len(left)): diff += abs(left[i] - right[i])
    print(diff)