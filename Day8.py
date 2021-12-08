def containCount(str, set):
    count = 0
    for c in set:
        if c in str:
            count += 1
    return count


file1 = open('inputs/input8.txt', 'r')
lines = file1.readlines()

current = ''
total = 0

for line in lines:
    command = line.split('|')
    decode = command[0].split()
    mapping = {}
    for num in decode:
        if len(num) == 2:
            mapping[2] = set(list(num))
        if len(num) == 3:
            mapping[3] = set(list(num))
        if len(num) == 4:
            mapping[4] = set(list(num))

    print(mapping)

    current = ''
    output = command[1].split()
    for num in output:
        if len(num) == 2:
            current += '1'
        elif len(num) == 3:
            current += '7'
        elif len(num) == 4:
            current += '4'
        elif len(num) == 5:
            if (2 in mapping and containCount(num, mapping[2]) == 1) or \
                    (3 in mapping and containCount(num, mapping[3]) == 2):
                if containCount(num, mapping[4]) == 3:
                    current += '5'
                else:
                    current += '2'
            else:
                current += '3'
        elif len(num) == 6:
            if (2 in mapping and containCount(num, mapping[2]) == 1) or \
                    (3 in mapping and containCount(num, mapping[3]) == 2):
                current += '6'
            else:
                if containCount(num, mapping[4]) == 3:
                    current += '0'
                else:
                    current += '9'
        elif len(num) == 7:
            current += '8'

    total += int(current)
    print(total, int(current), output)

print(total)
