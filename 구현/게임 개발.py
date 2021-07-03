n,m = map(int,input().split())

x,y,direction =map(int,input().split())
d=[[0]*m for i in range(n)]


array=[]
for i in range(n):
    array.append(list(map(int,input().split())))

# 북 동 남 서
dx=[-1,0,1,0]
dy=[0,1,0,-1]


def turn_left():
    global direction
    direction =(direction-1)%4


d[x][y] = 1
count=1
turn_time = 0

while True:
    turn_left()
    nx=x+dx[direction]
    ny=y+dy[direction]
    # 맵의 외각은 항상 바다로 되엉있으므로 필요 없음
    #if nx>=0 and nx<n and ny>=0 and ny<m:
    #육지이고 가본적 없는 경우
    if array[nx][ny]==0 and d[nx][ny]==0:
        x,y=nx,ny
        count+=1
        d[nx][ny]=1
        turn_time=0
    else:
        turn_time+=1

    if turn_time>=4:
        nx=x-dx[direction]
        ny = y - dy[direction]
        if array[nx][ny]==1:
            break
        x,y=nx,ny
        turn_time=0
print(count)