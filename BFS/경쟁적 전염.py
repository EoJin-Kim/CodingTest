from collections import deque
n,k = map(int,input().split())

array=[[] for _ in range(n)]
dx=[-1,0,1,0]
dy=[0,1,0,-1]
for i in range(n):
    data=list(map(int,input().split()))
    for j in data:
        array[i].append((j,0))


s,resultX,resultY=map(int,input().split())
virus=[]
for i in range(n):
    for j in range(n):
        if array[i][j][0]!=0:
            virus.append((array[i][j][0],0,i,j))


virus.sort()
q=deque(virus)
def bfs():


    while q:
        typ ,sec,x,y = q.popleft()
        if sec==s:
            break
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]

            if nx>=0 and nx<n and ny>=0 and ny<n:
                if array[nx][ny][0]==0:
                    array[nx][ny]=(typ,sec+1)
                    q.append((typ,sec+1,nx,ny))

bfs()
result=array[resultX-1][resultY-1]
if result[0]==0 or result[1]>s:
    print(0)
else:
    print(result[0])