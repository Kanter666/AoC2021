file1 = open('inputs/input4.txt', 'r')
lines = file1.readlines()


def check_bing(check_board, i, j):
    if sum(check_board[i]) == 5:
        return 1
    row_sum = 0
    for r in range(5):
        row_sum += check_board[r][j]
    if row_sum == 5:
        return 2
    return 0


numbers = [int(x) for x in lines[0].split(',')]
boards = []
checked = []
for line in lines[1:]:
    if len(line) > 1:
        boards[-1].append([int(x) for x in line.split()])
        checked[-1].append([0]*5)
    else:
        boards.append([])
        checked.append([])
print(len(boards), boards, checked)

for num in numbers:
    print('-------------')
    print(num)
    for idx, board in enumerate(boards):
        for i in range(5):
            if num in board[i]:
                pos = board[i].index(num)
                checked[idx][i][pos] = 1
                print(boards[idx], checked[idx])
                result = check_bing(checked[idx], i, pos)
                if result:
                    print(board)
                    if result == 1:
                        print(1)
                        print(sum(board[i])*num)
                        quit()
                    elif result == 2:
                        total = 0
                        for row in range(5):
                            for col in range(5):
                                if not checked[idx][row][col]:
                                    total += board[row][col]
                        print(2)
                        print(total*num)
                        quit()

