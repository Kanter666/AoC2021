file1 = open('inputs/input2.txt', 'r')
lines = file1.readlines()

depth, position = 0, 0
for line in lines:
    command = line.split()
    if command[0] == "down":
        depth += int(command[1])
    elif command[0] == "up":
        depth -= int(command[1])
    elif command[0] == "forward":
        position += int(command[1])
    print(command, depth, position)

print(depth*position)
