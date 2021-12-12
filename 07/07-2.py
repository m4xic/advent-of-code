with open('07', 'r') as f: crabs = [int(x) for x in f.read().split(',')]
#print(crabs)

totals = {}
for pos in range(0, max(crabs)):
    pos_total = 0
    for crab in crabs:
        pos_total += sum(range(abs(crab - pos)+1))
    totals[pos] = pos_total

print(sorted(totals.items(), key = lambda i: i[1]))