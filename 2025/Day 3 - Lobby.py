'''
# Part 1

banks = []
total = 0

with open("2025/data/day3.txt") as file:
    for line in file:
        banks.append([int(val) for val in list(line.strip())])

for bank in banks:
    index = bank.index(max(bank[:-1]))
    first = bank.pop(index)
    second = max(bank[index:])
    total += first * 10 + second

print(total)
'''


# Part 2

banks = []
total = 0

with open("2025/data/tester.txt") as file:
    for line in file:
        banks.append([int(val) for val in list(line.strip())])

for bank in banks:
    index = bank.index(max(bank[:-1]))
    first = bank.pop(index)
    second = max(bank[index:])
    total += first * 10 + second

print(total)
