file1 = open('inputs/input10.txt', 'r')
lines = file1.readlines()

scores = []
points = {
    ")": 1,
    "]": 2,
    "}": 3,
    ">": 4
}
match = {
    "(": ")",
    "[": "]",
    "{": "}",
    "<": ">",
}
for line in lines:
    stack = []

    error = False
    for char in list(line[:-1]):
        if char in match:
            stack.append(match[char])
        else:
            if stack and char == stack[-1]:
                stack.pop()
            else:
                error = True
                break
    if not error:
        print('-----')
        print(line)
        print(stack)
        score = 0
        for missing in stack[::-1]:
            score = score*5 + points[missing]
            print(missing, score)
        scores.append(score)

    print(char, scores)

scores.sort()
print(scores)
print(len(scores), len(scores)//2)

print(scores[len(scores)//2])
