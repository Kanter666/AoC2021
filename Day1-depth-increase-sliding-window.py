file1 = open('inputs/input1-depth.txt', 'r')
lines = file1.readlines()

increases = 0
currentDepth = int(lines[0])+int(lines[1])+int(lines[2])
for line in lines[2:]:
    nextDepthh = int(line)  # Or whatever prompt you prefer to use.
    print(currentDepth, nextDepthh, nextDepthh > currentDepth)
    if nextDepthh > currentDepth:
        increases += 1
    currentDepth = nextDepthh
print(increases)