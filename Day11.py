file1 = open('inputs/input11.txt', 'r')
lines = file1.readlines()

values = []
for line in lines:
    octopus = [int(x) for x in line[:-1]]
    values.append(octopus)
    print(values)

count = 0
stop = False
step = 0
while not stop:
    step += 1
    for i in range(len(values)):
        for j in range(len(values[0])):
            values[i][j] += 1

    for x in range(len(values)):
        for y in range(len(values[0])):
            if values[x][y] > 9:
                flashing = [[x, y]]
                while flashing:
                    i, j = flashing.pop()
                    count += 1
                    values[i][j] = 0
                    for l in values:
                        print(l)

                    if i > 0 and j > 0 and values[i-1][j-1]:
                        values[i - 1][j - 1] += 1
                        if values[i-1][j-1] > 9 and [i-1,j-1] not in flashing:
                            flashing.append([i-1, j-1])

                    if i > 0 and values[i-1][j]:
                        values[i - 1][j] += 1
                        if values[i-1][j] > 9 and [i-1,j] not in flashing:
                            flashing.append([i-1, j])

                    if i > 0 and j < len(values[0])-1 and values[i-1][j+1]:
                        values[i-1][j+1] += 1
                        if values[i-1][j+1] > 9 and [i-1,j+1] not in flashing:
                            flashing.append([i-1, j+1])

                    if j > 0 and values[i][j-1]:
                        values[i][j - 1] += 1
                        if values[i][j-1] > 9 and [i,j-1] not in flashing:
                            flashing.append([i, j-1])

                    if j > 0 and i < len(values)-1 and values[i+1][j-1]:
                        values[i + 1][j - 1] += 1
                        if values[i+1][j-1] > 9 and [i+1,j-1] not in flashing:
                            flashing.append([i+1, j-1])

                    if i < len(values)-1 and values[i+1][j]:
                        values[i + 1][j] += 1
                        if values[i+1][j] > 9 and [i+1,j] not in flashing:
                            flashing.append([i+1, j])
                    if j < len(values[0]) - 1 and values[i][j + 1]:
                        values[i][j + 1] += 1
                        if values[i][j + 1] > 9 and [i,j + 1] not in flashing:
                            flashing.append([i, j + 1])
                    if i < len(values)-1 and j<len(values[0])-1 and values[i+1][j+1]:
                        values[i+1][j+1] += 1
                        if values[i+1][j+1] > 9 and [i+1,j+1] not in flashing:
                            flashing.append([i+1, j+1])

    stop = True
    for i in range(len(values)):
        for j in range(len(values[0])):
            if values[i][j] != 0:
                stop = False

print(step)
