from itertools import combinations
n=int(input())
array=[]
for i in range(n):
    array.append(list(input().split()))


dx=[-1,0,1,0]
dy=[0,1,0,-1]
empty=[]
teacher=[]
for i in range(n):
    for j in range(n):
        if array[i][j]=="X":
            empty.append((i,j))
        elif array[i][j]=="T":
            teacher.append((i,j))

def FindStudent():
    for x,y in teacher:
        for i in range(4):
            count = 1
            nx = x + dx[i]*count
            ny = y + dy[i]*count
            while nx>=0 and nx<n and ny>=0 and ny<n:
                if array[nx][ny]=="O":
                    break
                elif array[nx][ny]=="S":
                    return True
                count+=1
                nx = x + dx[i]*count
                ny = y + dy[i]*count
    return False


result=False
for wall in combinations(empty,3):
    for x,y in wall:
        array[x][y]="O"

    if not FindStudent():
        result=True
        break
    for x,y, in wall:
        array[x][y]="X"


if result:
    print("YES")

else:
    print("NO")


'''
5
X S X X T
T X S X X
X X X X X
X T X X X
X X T X X

4
S S S T
X X X X
X X X X
T T T X
'''