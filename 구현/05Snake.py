
n = int(input())
k = int(input())
array=[[0] * (n+1) for _ in range(n+1)]
info=[]
for _ in range(k):
    x,y=map(int,input().split())
    array[x][y] = 1
command= int(input())

for _ in range(command):
    t,m=input().split()
    info.append((int(t),m))

#처음에 오른쪽 보고있으니까
# 동 남 서 북
dx=[0,1,0,-1]
dy = [1,0,-1,0]
direction=0

#현재 방향 입력받아 +1 후 4로 나눈 나머지가 방향으로 리턴
def turn(direction,c):
    if c=="L":
        direction = (direction-1)%4
    else:
        direction = (direction+1)%4
    return direction

def simulate():
    #뱀의 머리
    x,y = 1,1
    #뱀이 존재하면 2
    array[x][y] =2
    direction = 0
    time = 0
    #꼬리부터 머리 순서
    body =[(x,y)]
    #명령 실행한 횟수
    index=0
    while True:
        nx = x+dx[direction]
        ny = y+dy[direction]
        #벽이나 몸통이 아닐 경우
        if nx>= 1 and nx<= n and ny >=1 and ny<=n and array[nx][ny]!=2:
            # 빈 공간
            if array[nx][ny] == 0:
                array[nx][ny] = 2
                body.append((nx, ny))
                px,py=body.pop(0)
                array[px][py]=0

            # 사과
            elif array[nx][ny] == 1:
                array[nx][ny] = 2
                body.append((nx, ny))
            x, y = nx, ny
        else:
            time+=1
            break

        time +=1

        if index<command and info[index][0]==time:
            direction = turn(direction,info[index][1])
            index+=1
    return time
print(simulate())