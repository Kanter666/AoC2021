file1 = open('inputs/input10.txt', 'r')
lines = file1.readlines()

score = 0
points = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137,
}
match = {
    "(": ")",
    "[": "]",
    "{": "}",
    "<": ">",
}
for line in lines:
    stack = []

    for char in list(line[:-1]):
        if char in match:
            stack.append(match[char])
        else:
            if stack and char == stack[-1]:
                stack.pop()
            else:
                score += points[char]
                break

    print(char, score)

print(score)
