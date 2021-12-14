from collections import Counter

with open('14-t', 'r') as f: template = list(f.read())
with open('14-r', 'r') as f: rules = [tuple(g.split(' -> ')) for g in f.read().splitlines()]

i, j, steps = 0, 0, 0

while steps < 10:
    print(f"*** Starting step {steps+1}...")
    print(f"*** template=" + ''.join(template))
    print('---')
    i = 0
    while i < len(template) - 1:
        #print(f"{template[i]}{template[i+1]}")
        j, skip = 0, False
        while j < len(rules):
            #print(f"{i=} {j=} {len(template)=}")
            rule, add = tuple(rules[j][0]), rules[j][1]
            if template[i] == rule[0] and template[i+1] == rule[1]:
                #print(f"MATCHED!  {template[i]}{template[i+1]}  {rule=} {add=}")
                template.insert(i+1, add)
                i += 2
                skip = True
                break # I put this in and it worked. Don't ask me why
            #print(f"{rule=}")
            j += 1
        if skip == False: i += 1
    steps += 1
print(''.join(template))
c = Counter(template)
print(c)
#print("NBBNBNBBCCNBCNCCNBBNBBNBBBNBBNBBCBHCBHHNHCBBCBHCB")