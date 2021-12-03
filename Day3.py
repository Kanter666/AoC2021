file1 = open('inputs/input3.txt', 'r')
lines = file1.readlines()

count = 0
position = 0
while len(lines) > 1:
    next_lines = []
    for line in lines:
        count += int(line[position])
    half = len(lines)/2
    current = 1 if count >= half else 0

    for line in lines:
        if int(line[position]) == current:
            next_lines.append(line)

    lines = next_lines
    position += 1
    count = 0

oxygen = lines[0]
print(oxygen)

file1 = open('inputs/input3.txt', 'r')
lines = file1.readlines()
count = 0
position = 0
while len(lines) > 1:
    next_lines = []
    for line in lines:
        count += int(line[position])
    half = len(lines) / 2
    current = 1 if count < half else 0

    for line in lines:
        if int(line[position]) == current:
            next_lines.append(line)

    lines = next_lines
    position += 1
    count = 0

CO2 = lines[0]

print(oxygen, CO2, int(oxygen, 2), int(CO2, 2))
print(int(oxygen, 2)*int(CO2, 2))
