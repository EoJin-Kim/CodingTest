from collections import deque
n,l,r=map(int,input().split())

array=[]
for i in range(n):
    array.append(list(map(int,input().split())))

dx=[-1,0,1,0]
dy=[0,1,0,-1]
def bfs(x,y,index):
    total=array[x][y]
    count =1
    union=[(x,y)]
    q=deque()
    q.append((x,y))
    united[x][y]=index
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx>=0 and nx<n and ny>=0 and ny<n and united[nx][ny]==-1:
                if l<=abs(array[x][y]-array[nx][ny])<=r:
                    united[nx][ny]=index
                    union.append((nx,ny))
                    q.append((nx,ny))
                    total+=array[nx][ny]
                    count+=1


    for i,j in union:
        array[i][j]=total//count




totalCount=0

while True:
    united = [[-1] * n for _ in range(n)]
    index = 0
    for i in range(n):
        for j in range(n):
            if united[i][j]==-1:
                bfs(i,j,index)
                index+=1

    # 모든 나라가 변경 사항이 없으면 index = n*n
    if index==n*n:
        break
    totalCount+=1

print(totalCount)