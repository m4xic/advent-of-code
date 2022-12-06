import sys
with open('input', 'r') as fp:
    file = fp.read().strip()

# part a
msg_length = 4
#  part b
#msg_length = 14

for i in range(len(file)):
    chars = list(file[i:i+msg_length])
    print(chars)
    if len(set(chars)) == msg_length:
        print(i+msg_length)
        sys.exit()
