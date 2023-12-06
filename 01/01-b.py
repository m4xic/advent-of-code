with open("input", "r") as f:
    lines = f.readlines()

new_input = []
replacements = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}

for line in lines:
    line = line.strip()
    new_line = ""
    for letter in line:
        new_line += letter
        for replacement in replacements.keys():
            if new_line.endswith(replacement):
                new_line = new_line.replace(replacement, replacements[replacement])
    print(f'"{line}" -> "{new_line}"')
    new_input.append(new_line)

with open("input2", "w+") as f:
    f.write("\n".join(new_input))
