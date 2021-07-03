n,m = map(int,input().split())
array=[]
for i in range(n):
    array.append(list(map(int,input())))

count=0
dx=[-1,0,1,0]
dy=[0,1,0,-1]



def dfs(x,y):

    if array[x][y]==0:
        array[x][y]=1
        for i in range(4):
            nx = x+dx[i]
            ny= y +dy[i]
            if nx>=0 and nx<n and ny>=0 and ny < m:
                dfs(nx,ny)
        return True
for i in range(n):
    for j in range(m):
        if dfs(i,j):
            count +=1
print(count)