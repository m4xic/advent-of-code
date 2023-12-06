with open("input", "r") as f:
    lines = f.readlines()

all_numbers = []
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
    print(line)
    new_line = ""
    this_line = []
    for letter in line:
        new_line += letter
        if letter.isdigit():
            print(f"{letter} is a digit")
            this_line.append(letter)
        else:
            for replacement in replacements:
                if new_line.endswith(replacement):
                    print(f"{new_line} ends with {replacement}")
                    this_line.append(replacements[replacement])
    all_numbers.append(this_line)

print(all_numbers)

with open("input3", "w+") as f:
    for line in all_numbers:
        f.write("".join(line) + "\n")
