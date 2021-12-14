with open('14-t', 'r') as f: temp_template = list(f.read())
with open('14-r', 'r') as f: temp_rules = [tuple(g.split(' -> ')) for g in f.read().splitlines()]

# setup
template, rules = {}, {}
for i in range(len(temp_template)-1):
    if (temp_template[i], temp_template[i+1]) in template.keys(): template[(temp_template[i], temp_template[i+1])] += 1
    else: template[(temp_template[i], temp_template[i+1])] = 1

for j in range(len(temp_rules)):
    print(f"{temp_rules[j]}")
    letter_1 = list(temp_rules[j][0])[0]
    letter_2 = list(temp_rules[j][0])[1]
    add = temp_rules[j][1]
    print(f"{letter_1=} {letter_2=} {add=}")
    print()
    rules[(letter_1, letter_2)] = [(letter_1, add), (add, letter_2)]
print(template)
print()
print(rules)

steps = 1
while steps < 41:
    print(f"Step {steps} starting")
    copy_dict = dict(template)
    for matched_rule in rules.keys():
        if matched_rule in copy_dict.keys():
            if copy_dict[matched_rule] == 0: continue
            amount = copy_dict[matched_rule]
            template[matched_rule] -= amount
            for each_replacement in rules[matched_rule]:
                if each_replacement in template.keys(): template[each_replacement] += amount
                else: template[each_replacement] = amount
    steps += 1
    print(f"Length: {int((sum(template.values()) * 2) * (3 / 2))}")

letters = {}
for pair in template.keys():
    for letter in pair:
        if letter not in letters.keys(): letters[letter] = template[pair]
        else: letters[letter] += template[pair]

for letter in letters.keys(): letters[letter] = letters[letter] / 2
print(letters)
print(sorted(letters.items(), key=lambda n:n[1]))

# this shouldn't work somewhere along the way the calculation is wrong and it ends up with decimals... but it all evens out I guess? My most common and least common (K and F) both had .5 so subtracting them together gave a whole number and eventually gave the correct answer 🤷🏽‍♂️

#{'K': 193200271244.5, 'H': 206420145579.0, 'S': 252943215762.0, 'C': 422415532942.0, 'P': 6287180922765.0, 'F': 12464638059774.5, 'B': 211999150163.0, 'O': 198828019091.0, 'V': 274816464465.0, 'N': 378279145958.0}

#[('K', 193200271244.5), ('O', 198828019091.0), ('H', 206420145579.0), ('B', 211999150163.0), ('S', 252943215762.0), ('V', 274816464465.0), ('N', 378279145958.0), ('C', 422415532942.0), ('P', 6287180922765.0), ('F', 12464638059774.5)]