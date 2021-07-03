from collections import deque
dx=[[-1,-1,0],[0,1,1],[1,1,0],[0,-1,-1]]
dy=[[0,1,1],[1,1,0],[0,-1,-1],[-1,-1,0]]

def solution(m, n, board):

    answer = 0
    temp=[]
    for b in board:
        temp.append(list(b))

    board=temp
    #print(board)
    #4개 짜리 있는지 확인
    while True:
        boomSet=set()
        for x in range(m):
            for y in range(n):
                now=board[x][y]
                if board[x][y]=="0":
                    continue
                for a in range(4):
                    cnt=0
                    for b in range(3):
                        nx=x+dx[a][b]
                        ny=y+dy[a][b]
                        if nx>=0 and nx<m and ny>=0 and ny<n:
                            if board[nx][ny]==now:
                                cnt+=1
                    # 4개이면 주변 확산
                    if cnt==3:
                        boom=[(x,y)]
                        for b in range(3):
                            boomSet.add((x+dx[a][b],y+dy[a][b]))
        if len(boomSet)==0:
            break

        answer += len(boomSet)
        Boom(board,boomSet)
        Down(board,m,n)

    return answer

def Boom(board,boom):
    boom=list(boom)
    count=0
    for x,y in boom:
        board[x][y]="0"


def Down(board,m,n):
    while True:
        check=False
        for x in range(m-1):
            for y in range(n):
                if board[x][y]!="0" and board[x+1][y]=="0":
                    board[x+1][y],board[x][y]=board[x][y],board[x+1][y]
                    check=True
        if check==False:
            break
    return False

    #print(boom)

#m = 4;  n = 5;  board = ["CCBDE", "AAADE", "AAABF", "CCBBF"]
#print( solution(m, n , board) ) # 14
#m = 6;  n = 6;  board = ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]
#print( solution(m, n , board) ) # 15
#m = 6; n = 6; board = ["OXXOXX", "OXXXXX", 'OOXXXX', 'OXXOXX', 'OXXXXX', 'OOXXXX']
#print( solution(m, n, board) ) # 30

m = 6; n = 6; board = ['AABBEE','AAAEEE','VAAEEV','AABBEE','AACCEE','VVCCEE' ]
print( solution(m, n, board) ) # 32


print( solution(3,2, ["AA", "AA", "AB"])) # 4
print( solution(4,2, ["CC", "AA", "AA", "CC"]) )  # 8

print(solution(6,2, ["DD", "CC", "AA", "AA", "CC", "DD"]) )# 12
print(solution(8,2, ["FF", "AA", "CC", "AA", "AA", "CC", "DD", "FF"]) )# 8
print(solution(6,2, ["AA", "AA", "CC", "AA", "AA", "DD"])) # 8

print( solution(2,2,["AA", "AA"]) ) # 4
print( solution(2,2, ["AA", "AB"]) ) # 0
