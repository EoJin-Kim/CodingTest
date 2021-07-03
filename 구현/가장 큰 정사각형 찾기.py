from itertools import chain


def solution(board):
    answer = 0
    row = len(board)
    col = len(board[0])
    for i in range(1, row):
        for j in range(1, col):
            if board[i][j] != 0:
                board[i][j] = min(board[i - 1][j], board[i - 1][j - 1], board[i][j - 1]) + 1
    return (max(chain(*board))) ** 2


'''
def solution(board):
    answer = 0
    row = len(board)
    col = len(board[0])
    maxLen = max(row, col)

    for x in range(maxLen,0,-1):
        if FindSquare(x, board):
            answer=x
            return answer**2
    return answer


def FindSquare(lenX,board):
    row = len(board)
    col = len(board[0])
    for i in range(row - lenX + 1):
        for j in range(col - lenX + 1):
            temp = [br[j:j + lenX] for br in board[i:i + lenX]]
            tmpTotal = chain(*temp)
            if 0 in tmpTotal:
                continue
            else:
                return True
    return False
'''
#print(solution([[0, 1, 1, 1],[1, 1, 1, 1],[1, 1, 1, 1],[0, 0, 1, 0]]))
#print(solution([[0, 0, 1, 1], [1, 1, 1, 1]]))
#print(solution([[0]]))
#print(solution([[0, 0, 0], [0, 0, 0]]))