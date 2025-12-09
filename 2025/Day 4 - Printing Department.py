'''
# Part 1

shifts = [(1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1)]
grid = []
count = 0

with open("2025/data/day4.txt") as file:
    for line in file:
        grid.append([char for char in line.strip()])

for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] != "@":
            continue
        neighbors = 0
        for shift_x, shift_y in shifts:
            new_y, new_x = i + shift_y, j + shift_x
            if 0 <= new_y < len(grid) and 0 <= new_x < len(grid[i]) and grid[new_y][new_x] == "@":
                neighbors += 1
        if neighbors < 4:
            count += 1

print(count)
'''

# Part 2

shifts = [(1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1)]
grid = []
previous = []
count = 0

with open("2025/data/tester.txt") as file:
    for line in file:
        grid.append([char for char in line.strip()])

while grid != previous:
    removed = []
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] != "@":
                continue
            neighbors = 0
            for shift_x, shift_y in shifts:
                new_y, new_x = i + shift_y, j + shift_x
                if 0 <= new_y < len(grid) and 0 <= new_x < len(grid[i]) and grid[new_y][new_x] == "@":
                    neighbors += 1
            if neighbors < 4:
                count += 1
                removed.append((i, j))
    for y, x in removed:
        grid[y][x] = "."

print(count)
