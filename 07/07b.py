# used      42143088
# total     70000000
# need      30000000
# delta     27856912

# delete    2143088

# subdirs is a file created from 07-a.py

with open('subdirs', 'r') as fp:
    file = [i.strip() for i in fp.readlines()]

subdirs = {}
for dir in file:
    _, name, size = dir.split(' ')
    subdirs[name] = int(size)

sorted_subdirs = sorted(subdirs.items(), key=lambda x: x[1])

for subdir in sorted_subdirs:
    print(subdir[0], subdir[1])
    if subdir[1] > 2143088:
        print("!!", subdir[0], subdir[1])
