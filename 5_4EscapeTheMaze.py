from collections import deque
n,m =map(int,input().split())
graph=[]
for i in range(n):
    graph.append(list(map(int,input())))
#상 하 좌 우
dx=[0,0,-1,1]
dy=[-1,1,0,0]
print(graph)

def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if nx<0 or ny <0 or nx>=m or ny >=n:
                continue
            elif graph[ny][nx] ==0:
                continue
            elif graph[ny][nx]==1:
                graph[ny][nx] = graph[y][x]+1
                queue.append((nx,ny))
    return graph[n-1][m-1]

print(bfs(0,0))