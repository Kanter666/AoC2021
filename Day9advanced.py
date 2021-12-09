file1 = open('inputs/input9.txt', 'r')
lines = file1.readlines()

points = []
visited = []

for line in lines:
    points.append([int(x) for x in list(line[:-1])])
    visited.append([0]*len(line))

multiply = 0
sizes = []
for x in range(len(points)):
    for y in range(len(points[0])):
        if points[x][y]==9 or visited[x][y]==1:
            continue

        print('START: ', x, y, points[x][y], visited[x][y])
        size = 0
        stack = [[x, y]]
        visited[x][y] = 1

        while stack:
            size += 1
            pos = stack.pop()
            i, j = pos[0], pos[1]
            print(points[i][j])
            print(visited[0])
            print(visited[1])
            print(visited[2])
            print('----')

            if i>0:
                if points[i-1][j]!=9 and visited[i-1][j]==0:
                    stack.append([i-1, j])
                    visited[i - 1][j] = 1
            if i<len(points)-1:
                if points[i+1][j]!=9 and visited[i+1][j]==0:
                    stack.append([i+1, j])
                    visited[i + 1][j] = 1

            if j>0:
                if points[i][j-1]!=9 and visited[i][j-1]==0:
                    stack.append([i, j-1])
                    visited[i][j-1] = 1
            if j < len(points[0]) - 1:
                if points[i][j+1]!=9 and visited[i][j+1]==0:
                    stack.append([i, j+1])
                    visited[i][j + 1] = 1

        print('SIZE ', size)
        sizes.append(size)

sizes.sort(reverse=True)
print(sizes)
print(sizes[0]*sizes[1]*sizes[2])
