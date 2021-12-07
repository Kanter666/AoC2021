import statistics

file1 = open('inputs/input7.txt', 'r')
lines = file1.readlines()

positions = [int(x) for x in lines[0].split(',')]

# positions = [16, 1, 2, 0, 4, 2, 7, 1, 2, 14]
mid = int(statistics.median(positions))

print(mid, positions)
fuel = 0
for num in positions:
    fuel += abs(num-mid)
print(fuel)
