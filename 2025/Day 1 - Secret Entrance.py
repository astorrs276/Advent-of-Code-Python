'''
# Part 1

zeroes = 0
current = 50

with open("2025/data/day1.txt") as file:
    for line in file:
        dir = line[0]
        dist = int(line.strip()[1:])
        if dir == "R":
            current += dist
        elif dir == "L":
            current -= dist
        current %= 100
        if current == 0:
            zeroes += 1

print(zeroes)
'''

# Part 2

zeroes = 0
current = 50
last_change = ""

with open("2025/data/day1.txt") as file:
    for line in file:
        previous = current
        dir = line[0]
        dist = int(line.strip()[1:])
        if dir == "L":
            if (current - dist) < 0:
                zeroes += abs((current - dist + 100) // 100)
                if current != 0:
                    zeroes += 1
            current = (current - dist) % 100
            if current == 0:
                zeroes += 1
        elif dir == "R":
            zeroes += (current + dist) // 100
            current = (current + dist) % 100
        last_change = dir

print(zeroes)
