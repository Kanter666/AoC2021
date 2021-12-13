file1 = open('inputs/input13.txt', 'r')
lines = file1.readlines()

points_x, points_y = [], []
folds = []
for line in lines:
    if ',' in line:
        y, x = [int(x) for x in line.split(',')]
        points_x.append(x)
        points_y.append(y)
    elif "fold along " in line:
        if "y" in line:
            folds.append(["y", int(line.split('=')[1])])
        elif "x" in line:
            folds.append(["x", int(line.split('=')[1])])

paper = [[0 for x in range(max(points_y)+1)] for y in range(max(points_x)+1)]

for i in range(len(points_x)):
    paper[points_x[i]][points_y[i]] = 1

for l in paper:
    print(l)

for f in range(len(folds)):
    axis = folds[f][0]
    position = folds[f][1]
    if axis == "y":
        print("Y =================")
        for i in range(1, len(paper) - position):
            print(position + i, position - i)
            for j in range(len(paper[0])):
                paper[position - i][j] = max(paper[position - i][j], paper[position + i][j])

        paper = paper[:position]
    elif axis == "x":
        print("X =================")
        for i in range(1, len(paper[0]) - position):
            print(position + i, position - i)
            for j in range(len(paper)):
                paper[j][position - i] = max(paper[j][position - i], paper[j][position + i])

        paper = [line[:position] for line in paper]

count = 0
for l in paper:
    print(l)
    count += sum(l)
print("TOTAL: ", count)


