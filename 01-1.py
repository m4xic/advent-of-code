"""
199
200
208
210
200
207
240
269
260
263
"""

with open('01', 'r') as f:
    numbers = f.read().splitlines()
    increased = 0
    for i in range(1, len(numbers)):
        if int(numbers[i-1]) < int(numbers[i]): increased += 1
print(increased)