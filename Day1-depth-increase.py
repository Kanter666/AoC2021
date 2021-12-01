file1 = open('inputs/input2.txt', 'r')
lines = file1.readlines()

increases = 0
d1, d2, d3 = int(lines[0]), int(lines[1]), int(lines[2])
for line in lines[3:]:
    d4 = int(line)  # Or whatever prompt you prefer to use.
    if sum([d1, d2, d3]) < sum([d4, d2, d3]):
        increases += 1
    d1, d2, d3 = d2, d3, d4
print(increases)