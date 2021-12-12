with open('10', 'r') as f: lines = f.read().splitlines()
pairs = {'(': ')',
         '{': '}',
         '<': '>',
         '[': ']'}

score = 0
for line in lines:
    stack = []
    line = list(line)
    #print(line)
    for character in line:
        #print(f"{character=}  {stack=}")
        if character in pairs.keys():
            stack.append(character)
        else:
            if character != pairs[stack[-1]]:

                if character == ")": score += 3
                elif character == "]": score += 57
                elif character == "}": score += 1197
                elif character == ">": score += 25137

                stack.append('CORRUPT')
                break
            else:
                stack.pop()
    if stack[-1] == "CORRUPT": print(f"Corrupt line! {line}")
    elif stack == []: print(f"Complete line! {line}")
    else: print(f"Incomplete line! {line}")

print(f"{score=}")