from collections import deque

n,m =map(int,input().split())
array=[]
for i in range(n):
    array.append(list(map(int,input())))

x,y,=0,0
dx=[-1,0,1,0]
dy=[0,1,0,-1]

def bfs(x,y):
    q= deque([(x,y)])

    while q:
        x,y=q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx >= 0 and nx < n and ny >= 0 and ny < m and array[nx][ny]==1:
                array[nx][ny]=array[x][y]+1
                q.append((nx,ny))






bfs(x,y)
print(array)
print(array[n-1][m-1])