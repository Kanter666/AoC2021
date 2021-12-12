from collections import defaultdict

file1 = open('inputs/input12.txt', 'r')
lines = file1.readlines()

graph = defaultdict(set)
small = set()
for line in lines:
    points = line[:-1].split('-')
    graph[points[0]].add(points[1])
    graph[points[1]].add(points[0])
    if points[0].islower():
        small.add(points[0])
    if points[1].islower():
        small.add(points[1])
print(graph)
print(small)

count = 0
paths = [["start", set(["start"])]]
while paths:
    node, visited = paths.pop()
    print("Start: ", node, visited)
    if node=="end":
        count += 1
    else:
        print(node)
        print(graph[node])
        for cave in graph[node]:
            if cave not in visited:
                current = visited.copy()
                if cave in small:
                   current.add(cave)
                paths.append([cave, current])

print(count)
