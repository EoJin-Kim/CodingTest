from collections import deque

INF=int(1e9)

array=[]
dx=[-1,0,1,0]
dy=[0,1,0,-1]
n=int(input())
for _ in range(n):
    array.append(list(map(int,input().split())))

now_size=2
now_x,now_y=0,0


for i in range(n):
    for j in range(n):
        if array[i][j]==9:
            now_x,now_y=i,j
            array[now_x][now_y]=0


def bfs():
    # 값이 -1이라면 도달할 수 없다는 의미 (최기화)
    dist=[[-1] * n for _ in range(n)]
    q=deque([(now_x,now_y)])
    dist[now_x][now_y]=0

    while q:
        x,y=q.popleft()

        for i in range(4):
            nx = x+dx[i]
            ny= y+dy[i]
            if nx>=0 and nx<n and ny >=0 and ny<n:
                # 자신의 크기보다 작거나 같은 경우, 아직 한번도 지나기지 않으면 이동 가능
                if dist[nx][ny] ==-1 and array[nx][ny]<=now_size:
                    dist[nx][ny]=dist[x][y]+1
                    q.append((nx,ny))
    return dist

#최단 거리 테이블이 주어졌을 때 , 먹을 물고기 찾는 함수
def find(dist):
    x,y=0,0
    min_dist=INF
    for i in range(n):
        for j in range(n):
            if dist[i][j]!=-1 and 1<=array[i][j] and array[i][j]<now_size:
                if dist[i][j]<min_dist:
                    x,y=i,j
                    min_dist=dist[i][j]
    if min_dist==INF:
        return None
    else:
        #먹을 수 있는 물고기 위치와 거리
        return x,y,min_dist

result=0
ate = 0

while True:
    a=bfs()
    value = find(a)
    if value == None:
        print(result)
        break

    # 현재 위치 갱신 및 이동 거리 변경
    else:
        now_x, now_y= value[0],value[1]
        result+=value[2]
        array[now_x][now_y] = 0
        ate+=1
        if ate>=now_size:
            now_size+=1
            ate=0

