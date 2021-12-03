def bin_to_dec(binary) -> int:
    bin_list = reversed(list(binary))
    actual, num = 0, 1
    for index in bin_list:
        if index == '1': actual += num
        num *= 2
    return actual

def main():
    with open('03', 'r') as f:
        lines = f.read().splitlines()

    most_common = ""
    least_common = ""

    for i in range(0, len(lines[0])):
        common = {}
        for line in lines:
            if line[i] in common.keys(): common[line[i]] += 1
            else: common[line[i]] = 1
        sort = sorted(common.items(), key=lambda x: x[1], reverse=True)
        most_common += sort[0][0]
        least_common += sort[-1][0]
    print(f"{most_common=} {least_common=}")
    most_common = bin_to_dec(most_common)
    least_common = bin_to_dec(least_common)
    print(f"{most_common=} {least_common=} {most_common*least_common=}")

main()
