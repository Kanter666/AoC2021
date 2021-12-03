file1 = open('inputs/input3.txt', 'r')
lines = file1.readlines()

bits = [0]*(len(lines[0])-1)
print(len(bits))
size = 0
print(bits)
for line in lines:
    size += 1

    for element in range(0, len(bits)):
        print(line[element])
        bits[element] += int(line[element])

size = size/2
print(bits)

gamma = [0]*len(bits)
epsilon = [0]*len(bits)
for i in range(0, len(bits)):
    if bits[i]>size:
        gamma[i] = 1
        epsilon[i] = 0
    else:
        gamma[i] = 0
        epsilon[i] = 1

print(gamma, epsilon)
print(int(''.join([str(x) for x in gamma]), 2)*int(''.join([str(x) for x in epsilon]), 2))
