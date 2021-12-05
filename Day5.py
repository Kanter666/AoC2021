file1 = open('inputs/input5.txt', 'r')
lines = file1.readlines()

sea = [[0]*999 for i in range(999)]
count = 0

for line in lines:
    points = line.split(' -> ')
    start = points[0].split(',')
    start_x, start_y = int(start[0]), int(start[1])
    end = points[1].split(',')
    end_x, end_y = int(end[0]), int(end[1])
    print(start, start_x, end, end_y)

    if start_x == end_x:
        start = min(start_y, end_y)
        end = max(start_y, end_y) + 1
        for y in range(start, end):
            if sea[start_x][y] == 1:
                count+=1
            sea[start_x][y] += 1
    elif start_y == end_y:
        start = min(start_x, end_x)
        end = max(start_x, end_x) + 1
        for x in range(start, end):
            if sea[x][start_y] == 1:
                count += 1
            sea[x][start_y] += 1
    else:
        if start_x < end_x:
            x_range = range(start_x, end_x+1)
        else:
            x_range = range(start_x, end_x-1, -1)
        if start_y < end_y:
            y_range = range(start_y, end_y + 1)
        else:
            y_range = range(start_y, end_y - 1, -1)

        for x, y in zip(x_range, y_range):
            print(x, y)
            if sea[x][y] == 1:
                count += 1
            sea[x][y] += 1
        print('not horizontal or vertical')

print(count)