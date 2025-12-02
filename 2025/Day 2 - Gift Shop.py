'''
# Part 1

total = 0

with open("2025/data/day2.txt") as file:
    ranges = [(pair.split("-")[0], pair.split("-")[1]) for pair in file.read().strip().split(",")]

for start, end in ranges:
    for num in range(int(start), int(end) + 1):
        if str(num)[:len(str(num)) // 2] == str(num)[len(str(num)) // 2:]:
            total += num


print(total)
'''

# Part 2

total = 0

with open("2025/data/day2.txt") as file:
    ranges = [(pair.split("-")[0], pair.split("-")[1]) for pair in file.read().strip().split(",")]

for start, end in ranges:
    for num in range(int(start), int(end) + 1):
        for i in range(1, len(str(num)) // 2 + 1):
            if len(str(num)) // (i) == len(str(num)) / (i):
                if str(num)[:i] * (len(str(num)) // (i)) == str(num):
                    total += num
                    break


print(total)