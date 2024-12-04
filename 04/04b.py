with open('input', 'r') as f: source = f.read().split('\n')

matrix = []

for y in source:
    row = []
    for x in range(len(y)):
        row.append(y[x])
    matrix.append(row)

print(matrix)

count = 0

# M A S is 3 long so
for y in range(len(matrix) - 2):
    for x in range(len(matrix[x]) - 2):
        print(f'{x},{y} = {matrix[y][x]}')

        tl = matrix[y][x]
        tr = matrix[y][x+2]
        mi = matrix[y+1][x+1]
        bl = matrix[y+2][x]
        br = matrix[y+2][x+2]

        if (tl == "M" and br == "S") or (tl == "S" and br == "M"):
            if (tr == "S" and bl == "M") or (tr == "M" and bl == "S"):
                if (mi == "A"):
                    count += 1

print(f'{count=}')