import numpy as np
import re

with open('input', 'r') as f: source = f.read().split('\n')

matrix = []

for y in source:
    row = []
    for x in range(len(y)):
        row.append(y[x])
    matrix.append(row)

print(matrix)

npm = np.matrix(matrix)
print(npm)

# No way I could've done this without numpy and this answer: https://stackoverflow.com/a/6313414
npdiags = [npm[::-1,:].diagonal(i) for i in range(-npm.shape[0]+1,npm.shape[1])]
npdiags.extend(npm.diagonal(i) for i in range(npm.shape[1]-1,-npm.shape[0],-1))
diags = [ i.tolist() for i in npdiags ]

print(diags)

total = 0

# Search rows
for y in matrix:
    row = ''.join(y)
    # This total adding thing shoulda been a function
    total += len(re.findall(r'XMAS', row))
    total += len(re.findall(r'XMAS', row[::-1]))

print(f'{total=}')

# Search columns
for x in range(len(matrix[0])):
    column = ''.join(npm[:, x].flatten().tolist()[0])
    total += len(re.findall(r'XMAS', column))
    total += len(re.findall(r'XMAS', column[::-1]))

print(f'{total=}')

# Search diagonals
for d in diags:
    diag = ''.join(d[0])
    total += len(re.findall(r'XMAS', diag))
    total += len(re.findall(r'XMAS', diag[::-1]))

print(f'{total=}')