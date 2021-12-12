import time

with open('10', 'r') as f: lines = f.read().splitlines()
pairs = {'(': ')',
         '{': '}',
         '<': '>',
         '[': ']'}

score = 0
incomplete_lines = []
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

                print('uh oh')
                stack.append('CORRUPT')
                break
            else:
                stack.pop()
    if stack[-1] == "CORRUPT":
        pass
    else:
        pass
        incomplete_lines.append((line, stack))

overall_autocomplete_score = []
#print(incomplete_lines)
for inc_line, stack in incomplete_lines:
    print(f"Starting to process line {''.join(inc_line)}")
    line_score = 0
    for character in stack[::-1]:
        line_score = line_score * 5
        if character == "(": line_score += 1
        elif character == "[": line_score += 2
        elif character == "{": line_score += 3
        elif character == "<": line_score += 4
        print(f"{character=}  {line_score=}")
    overall_autocomplete_score.append(line_score)
    print(f"{''.join(inc_line)}  {stack}  {line_score=}")
    #input()
print(f"{overall_autocomplete_score}")
oac = sorted(overall_autocomplete_score)
print(oac[(len(oac)//2)])