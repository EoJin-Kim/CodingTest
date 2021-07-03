# n 맵 크기, m 상어 개수, k 냄새 시간
n,m,k=map(int,input().split())

# 상어 위치만 표시
array=[]
for i in range(n):
    array.append(list(map(int,input().split())))


directions = list(map(int,input().split()))

# 각 위치마다 [특정 냄새의 상어 번호, 특정 냄새의 남은 시간]을 저장하는 2차원 리스트
smell=[[[0,0]]*n for _ in range(n)]

# 각 상어의 회전 방향 우선순위 정보
priorities=[[] for _ in range(m)]
for i in range(m):
    for j in range(4):
        priorities[i].append(list(map(int,input().split())))

dx=[-1,1,0,0]
dy=[0,0,-1,1]



def update_smell():
    for i in range(n):
        for j in range(n):
            if smell[i][j][1]>0:
                smell[i][j][1]-=1

            # 상어가 존재하는 해당 위치의 냄새를 k로 설정
            if array[i][j] !=0:
                # array[i][j] 는 상어 번호
                smell[i][j]=[array[i][j],k]
def move():
    # 이동 결과를 담기 위한 임시 결과 테이블 초기화
    new_array= [[0] * n for _ in range(n)]

    for x in range(n):
        for y in range(n):
            # 상어가 존재하는 경우
            if array[x][y] !=0:
                direction=directions[array[x][y]-1]
                #갈 수 있는곳이 있는지 체크
                found = False
                # 일단 냄새가 존재하지 않는 곳이 있는지 확인
                for index in range(4):
                    # dirctions 3차원 배열 : 1. 어떤 상어, 어떤 방향 , 냄새가 존재하는지(index)방향의 우선순위 부터 냄새가 존재하지 않는지 확인
                    # dx는 0부터 시작이고 priorities 방향은 1부터 시작이므로 -1
                    nx = x + dx[priorities[array[x][y] - 1][direction-1][index]-1]
                    ny = y + dy[priorities[array[x][y] - 1][direction - 1][index] - 1]
                    if nx>=0 and nx<n and ny>=0 and ny<n:
                        # 냄새가 없으면
                        if smell[nx][ny][1]==0:
                            # 방향 전환
                            directions[array[x][y]-1] = priorities[array[x][y] - 1][direction - 1][index]
                            # 빈 공간이라면
                            if new_array[nx][ny]==0:
                                new_array[nx][ny]=array[x][y]

                            # 이미 다른상어가 있다면 작은 숫자 상어 존재
                            else:
                                new_array[nx][ny]=min(new_array[nx][ny],array[x][y])

                            # 이동을 하면 found = True
                            found =True
                            break
                if found:
                    continue

                # 주면에 모두 냄새가 남아 있다면 자신의 냄새가 있는 곳으로 이동
                for index in range(4):
                    nx = x + dx[priorities[array[x][y] - 1][direction - 1][index] - 1]
                    ny = y + dy[priorities[array[x][y] - 1][direction - 1][index] - 1]
                    if nx >= 0 and nx < n and ny >= 0 and ny < n:
                        # 내 냄새면 되돌아 이동
                        if smell[nx][ny][0]==array[x][y]:
                            directions[array[x][y]-1] = priorities[array[x][y] - 1][direction - 1][index]
                            new_array[nx][ny]=array[x][y]
                            break
    return new_array



time = 0
while True:
    update_smell()
    new_array=move()
    array=new_array
    time+=1
    check=True
    for i in range(n):
        for j in range(n):
            if array[i][j]>1:
                check=False
    if check:
        print(time)
        break

    if time>=1000:
        print(-1)
        break
