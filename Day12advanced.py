from collections import defaultdict
import copy

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
paths = [["start", set(["start"]), set(["start"])]]
while paths:
    node, visited1, visited2 = paths.pop()
    print("Start: ", node, visited1, visited2)
    if node=="end":
        count += 1
    else:
        # print(node)
        # print(graph[node])
        for cave in graph[node]:
            if cave not in visited1 or (len(visited2)<2 and cave!="start"):
                current1 = copy.deepcopy(visited1)
                current2 = copy.deepcopy(visited2)
                if cave in small:
                    if cave not in current1:
                        current1.add(cave)
                    else:
                        current2.add(cave)
                print("End: ", cave, current1, current2)

                paths.append([cave, current1, current2])

print(count)
