from collections import deque
import copy
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
INF=int(1e9)

def FeedCar(board,direction):
    length = len(board)
    for i in range(length):
        for j in range(length):
            if board[i][j]==0:
                board[i][j]=INF
    board[0][0]=0
    q=deque([(0,0,direction)])


    while q:
        x,y,direction=q.popleft()
        now_direction=direction
        for i in range(4):
            direction=(direction+i)%4
            nx=x+dx[direction]
            ny=y+dy[direction]
            if nx>=0 and nx<length and ny>=0 and ny<length:
                if board[nx][ny]!=1:
                    if direction==now_direction:
                        feed=100
                    else:
                        feed=600
                    if board[nx][ny]>=board[x][y] + feed:
                        board[nx][ny]=board[x][y] + feed
                        q.append((nx,ny,direction))
    return board[length-1][length-1]
def solution(board):
    # 첫 번째 칸 미리 넣어두기
    testBoard=copy.deepcopy(board)
    a=FeedCar(board,1)
    b = FeedCar(testBoard, 2)
    return min(a,b)

#print(solution([[0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0],[0,0,0,0,0,1,0,0],[0,0,0,0,1,0,0,0],[0,0,0,1,0,0,0,1],[0,0,1,0,0,0,1,0],[0,1,0,0,0,1,0,0],[1,0,0,0,0,0,0,0]]))
#print(solution([[0, 0, 1, 0], [0, 0, 0, 0], [0, 1, 0, 1], [1, 0, 0, 0]]))
#print(solution([[0,0,0,0,0,0],[0,1,1,1,1,0],[0,0,1,0,0,0],[1,0,0,1,0,1],[0,1,0,0,0,1],[0,0,0,0,0,0]]))
#print(solution([[0, 0, 0, 0, 0], [0, 1, 1, 1, 0], [0, 0, 1, 0, 0], [1, 0, 0, 0, 1], [0, 1, 1, 0, 0]]))
tc=[[0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 1, 0, 0],
    [1, 0, 0, 0, 1],
    [0, 1, 1, 0, 0]]

print(solution(tc))
print(solution([[0, 0, 0, 0, 0], [0, 1, 1, 1, 0], [0, 0, 1, 0, 0], [1, 0, 0, 0, 1], [0, 1, 1, 0, 0]] ))#3000