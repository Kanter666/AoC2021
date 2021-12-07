import statistics

file1 = open('inputs/input7.txt', 'r')
lines = file1.readlines()

positions = [int(x) for x in lines[0].split(',')]

mid = int(statistics.mean(positions))

while True:
    left = mid - 1
    right = mid + 1

    fuel_m = 0
    for num in positions:
        steps = abs(num-mid)
        for i in range(steps):
            fuel_m += 1 + i

    fuel_l = 0
    for num in positions:
        steps = abs(num-left)
        for i in range(steps):
            fuel_l += 1 + i

    fuel_r = 0
    for num in positions:
        steps = abs(num-right)
        for i in range(steps):
            fuel_r += 1 + i

    print('loop resuls:')
    print(fuel_m, fuel_l, fuel_r)
    if fuel_m > fuel_l:
        mid = mid - 1
    elif fuel_m > fuel_r:
        mid = mid + 1
    else:
        print(fuel_m)
        break
