import copy
INF= int(1e9)
# 4 x 4크기의  정사각형에 존재하는 물고기의 번호(없으면 -1)와 뱡항 값을 담는 테이블
array=[[None] * 4 for _ in range(4)]

for i in range(4):
    data = list(map(int,input().split()))
    for j in range(4):
        # 각 위치마다 [물고기 번호, 방향]을 저장
        # dx,dy 인덱스가 0부터 시작하는데 문제에는 1부터시작, 그래서 -1
        array[i][j]=[data[j*2],data[j*2+1]-1]

dx=[-1,-1,0,1,1,1,0,-1]
dy=[0,-1,-1,-1,0,1,1,1]

def turn_left(direction):
    return (direction+1)%8


result = 0


def find_fish(array,index):
    for i in range(4):
        for j in range(4):
            if array[i][j][0]==index:
                return (i,j)
    return None
# 모든 물고기 회전 및 이동 함수


def move_all_fishes(array,now_x,now_y):
    for i in range(1,17):
        position = find_fish(array,i)
        if position !=None:
            x,y=position[0],position[1]
            direction = array[x][y][1]
            for j in range(8):
                nx = x+dx[direction]
                ny = y+dy[direction]
                if 0<=nx and nx<4 and ny >=0 and ny<4:
                    if not(nx == now_x and ny == now_y):
                        # 이동 가능한 방향으로 array 업데이트 하고 위치 변경
                        array[x][y][1] =direction
                        array[x][y],array[nx][ny]=array[nx][ny],array[x][y]
                        break
                direction = turn_left(direction)

#상어가 현재 위치에서 먹을 수 있는 모든 물고기 위치 반환
def get_possible_positions(array,now_x,now_y):
    positions=[]
    direction=array[now_x][now_y][1]
    # 총 4 x 4 이므로 상어는 여러번 이동 가능, 4번 이동 하고 범위 벗어나면 무시
    for i in range(4):
        now_x+=dx[direction]
        now_y+=dy[direction]

        if 0<=now_x and now_x<4 and now_y>=0 and now_y <4:
            if array[now_x][now_y][0] !=-1:
                positions.append((now_x,now_y))

    return positions



def dfs(array, now_x, now_y, total):
    global result
    array = copy.deepcopy(array)

    total +=array[now_x][now_y][0]
    # 방향을 남겨놔야 상어 이동방향 체크
    array[now_x][now_y][0]=-1

    # 현재 상어 방향(now_x,now_y)
    # 상어 이동 위치 찾기
    move_all_fishes(array,now_x,now_y)
    positions = get_possible_positions(array,now_x,now_y)
    # dfs 최종 재귀함수 결과값은 total에 저장 됨으로 이때까지 결과값 가장적은값(result) 와 total 비교해서 큰 값 result
    if len(positions)==0:
        result = max(result,total)
        return
    for next_x,next_y in positions:
        dfs(array,next_x,next_y,total)




dfs(array,0,0,0)
print(result)



