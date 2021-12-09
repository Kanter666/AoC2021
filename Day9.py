file1 = open('inputs/input9.txt', 'r')
lines = file1.readlines()

points = []

for line in lines:
    points.append([int(x) for x in list(line[:-1])])

lowsum = 0
for i in range(len(points)):
    for j in range(len(points[0])):
        if i>0 and points[i][j]>=points[i-1][j]:
                continue

        if i<len(points)-1 and points[i][j]>=points[i+1][j]:
                continue

        if j>0 and points[i][j]>=points[i][j-1]:
                continue
        if j < len(points[0]) - 1:
            if points[i][j] >= points[i][j+1]:
                continue

        lowsum += 1 + points[i][j]
for p in points:
    print(p)
print(lowsum)
