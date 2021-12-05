# please ignore this horrendous mess. it's tough out here trying to complete advent of code okay

def bin_to_dec(binary) -> int:
    bin_list = reversed(list(binary))
    actual, num = 0, 1
    for index in bin_list:
        if index == '1': actual += num
        num *= 2
    return actual

def bit_criteria(lines: list, prefer: str, commonality: int) -> str:
    """
    lines: list of lines in the file we're reading from
    prefer: the number (0/1) to prefer when breaking ties as a string
    commonality: 0 or -1 (0 for most common, -1 for least common)
    """
    i, prefix = 0, ""
    while len(lines) > 1 and i < len(lines[0]):
        # While there is more than 1 item in the list, we need to get rid of some!
        count = {'0': 0, '1': 0}
        for line in lines: count[line[i]] += 1
        if count['0'] == count['1']:
            winner = prefer
        else:
            count = sorted(count.items(), key=lambda x: x[1], reverse=True)
            winner = count[commonality][0]
        prefix += str(winner)
        #print(f"{count=} {prefix=}")
        j = 0
        while j < len(lines):
            if not lines[j].startswith(prefix):
                del(lines[j])
                j -= 1
            j += 1
        i += 1
        print(f"{lines=}, {prefix=}")
    return lines[0]

def main():
    with open('03', 'r') as f:
        lines = f.read().splitlines()

    print("--- OXYGEN ---")
    oxygen = bit_criteria(lines, "1", 0)
    print("\n\n\n")
    with open('03', 'r') as f:
        lines = f.read().splitlines()
    print("--- CO2 ---")
    co2 = bit_criteria(lines, "0", -1)

    print(f"{oxygen} {co2}")

    print(bin_to_dec(oxygen))
    print(bin_to_dec(co2))

main()
