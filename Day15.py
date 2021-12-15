import heapq

cave = []
pos = 0
for vert in range(5):
    file1 = open('inputs/input15.txt', 'r')
    lines = file1.readlines()
    for line in lines:
        cave.append([])
        command = list(line[:-1])

        for horz in range(5):
            for x in command:
                val = int(x) + horz + vert

                if val > 9:
                    val -= 9
                cave[pos].append(val)
        pos += 1

print("done")
for l in cave:
    print(l)

queue = []
heapq.heappush(queue, [0, 0, 0])
visited = []

while queue:
    step = heapq.heappop(queue)
    val, x, y = step[0], step[1], step[2]
    if x == len(cave)-1 and y == len(cave[0])-1:
        print("====================")
        print(val)
        break
    if x>0 and (x-1, y) not in visited:
        visited.append((x-1, y))
        heapq.heappush(queue, [val + cave[x-1][y], x-1, y])
    if y>0 and (x, y-1) not in visited:
        visited.append((x, y-1))
        heapq.heappush(queue, [val + cave[x][y-1], x, y-1])
    if x<len(cave)-1 and (x+1, y) not in visited:
        visited.append((x+1, y))
        heapq.heappush(queue, [val + cave[x+1][y], x+1, y])
    if y<len(cave[0])-1 and (x, y+1) not in visited:
        visited.append((x, y+1))
        heapq.heappush(queue, [val + cave[x][y+1], x, y+1])
    print(step)
