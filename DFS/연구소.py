from itertools import combinations
import copy
n,m=map(int,input().split())

array=[]

for i in range(n):
    array.append(list(map(int,input().split())))


virus=[]
empty=[]
dx= [-1,0,1,0]
dy = [0,1,0,-1]
for i in range(n):
    for j in range(m):

        if array[i][j]==0:
            empty.append((i,j))
        elif array[i][j]==2:
            virus.append((i,j))


def dfs():
    result=-1
    for ws in combinations(empty,3):

        for x,y in ws:
            array[x][y]=1

        tempArray = copy.deepcopy(array)
        for x, y in virus:
            infect(tempArray,x,y)

        temp = Save(tempArray)
        result = max(result, temp)

        for x, y in ws:
            array[x][y] = 0
    return result


def infect(array,x,y):
    for i in range(4):
        nx= x +dx[i]
        ny= y +dy[i]
        if nx>=0 and nx<n and ny>=0 and ny<m and array[nx][ny]==0:
            array[nx][ny]=2
            infect(array,nx,ny)



def Save(array):
    count=0
    for i in range(n):
        for j in range(m):
            if array[i][j]==0:
                count+=1
    return count

print(dfs())