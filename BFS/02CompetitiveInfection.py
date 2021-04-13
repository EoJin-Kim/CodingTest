from collections import deque

n,k = map(int,input().split())
graph=[]
data=[]
for i in range(n):
    graph.append(list(map(int,input().split())))

    for j in range(n):
        if graph[i][j] != 0:
            data.append((graph[i][j],0, i, j))

s,x,y = map(int,input().split())
'''

n,k=3,3
graph=[[1,0,2],[0,0,0],[3,0,0]]
s,x,y=2,3,2
'''
data.sort()
q=deque(data)


dx=[-1,0,1,0]
dy=[0,1,0,-1]
def bfs(seconds):

    while q:

        type,time,x,y =q.popleft()
        if seconds<=time:
            break;
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx>=0 and nx<n and ny>=0 and ny<n:
                if graph[nx][ny]==0:
                    graph[nx][ny]=type
                    q.append((type,time+1,nx,ny))



bfs(s)
print(graph[x-1][y-1])