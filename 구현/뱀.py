def turn_left(direction):
    direction =(direction-1)%4
    return direction


def turn_right(direction):
    direction =(direction+1)%4
    return direction

n = int(input())
k=int(input())

graph=[[0]*n for i in range(n)]
direction=0
dx =[0,1,0,-1]
dy=[1,0,-1,0]
for i in range(k):
    x,y=map(int,input().split())
    graph[x-1][y-1]=2
l=int(input())
info=[]
for i in range(l):
    time,oper=input().split()
    info.append((int(time),oper))

result =0
time=0
x,y =0,0
index=0
q=[]
graph[x][y]=1
q.append((x,y))
while True:
    nx= x+dx[direction]
    ny= y + dy[direction]
    # 움질일 수 있는 경우
    if nx>=0 and nx<n and ny>=0 and ny<n and graph[nx][ny]!=1:
        # 사과인 경우
        if graph[nx][ny]==2:
            graph[nx][ny] = 1
            q.append((nx,ny))
        # 빈 공간인 경우
        else:
            graph[nx][ny]=1
            q.append((nx,ny))
            px,py=q.pop(0)
            graph[px][py]=0

    else:
        time +=1
        break

    time += 1
    x=nx
    y=ny
    if index < l and time==info[index][0]:
        if info[index][1]=="D":
            direction =turn_right(direction)
        else:
            direction = turn_left(direction)
        index+=1


print (time)