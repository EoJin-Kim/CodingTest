from collections import deque

def get_next_pos(pos,board):
    next_pos=[]
    pos = list(pos)
    pos1_x,pos1_y,pos2_x,pos2_y = pos[0][0],pos[0][1],pos[1][0],pos[1][1]

    dx = [-1, 1, 0, 0]
    dy = [0, 0 , -1 , 1]
    for i in range(4):
        pos1_next_x,pos1_next_y,pos2_next_x,pos2_next_y = pos1_x+dx[i],pos1_y+dy[i],pos2_x+dx[i],pos2_y+dy[i]
        #이동하고자 하는 두 칸이 모두 비어있다면
        if board[pos1_next_x][pos1_next_y]==0 and board[pos2_next_x][pos2_next_y]==0:
            next_pos.append({(pos1_next_x,pos1_next_y),(pos2_next_x,pos2_next_y)})

    # 현재 로봇이 가로로 놓여 있는 경우
    if pos1_x==pos2_x:
        # 왼쪽으로 회전하거나 오른쪽으로 회전
        for i in [-1,1]:
            if board[pos1_x+i][pos1_y]==0 and board[pos2_x+i][pos2_y]==0:
                next_pos.append({(pos1_x,pos1_y),(pos1_x+i,pos1_y)})
                next_pos.append({(pos2_x , pos2_y),(pos2_x+i, pos2_y)})
    # 현재 로봇이 새로로 놓여 있는 경우
    elif pos1_y==pos2_y:
        # 왼쪽으로 회전하거나 오른쪽으로 회전
        for i in [-1, 1]:
            if board[pos1_x][pos1_y+i]==0 and board[pos2_x][pos2_y+i]==0:
                next_pos.append({(pos1_x,pos1_y),(pos1_x,pos1_y+i)})
                next_pos.append({(pos2_x, pos2_y), (pos2_x, pos2_y + i)})
    return next_pos

def solution(board):
    # 맵의 외곽에 벽을 두는 형태로 맵 변형
    n = len(board)
    new_board = [[1] * (n + 2) for _ in range(n + 2)]
    for i in range(n):
        for j in range(n):
            new_board[i + 1][j + 1] = board[i][j]
    # 너비 우선 탐색(BFS) 수행
    q = deque()
    visited = []
    pos = {(1, 1), (1, 2)} # 시작 위치 설정
    q.append((pos, 0)) # 큐에 삽입한 뒤에
    visited.append(pos) # 방문 처리
    # 큐가 빌 때까지 반복
    while q:
        pos, cost = q.popleft()
        # (n, n) 위치에 로봇이 도달했다면, 최단 거리이므로 반환
        if (n, n) in pos:
            return cost
        # 현재 위치에서 이동할 수 있는 위치 확인
        for next_pos in get_next_pos(pos, new_board):
            # 아직 방문하지 않은 위치라면 큐에 삽입하고 방문 처리
            if next_pos not in visited:
                q.append((next_pos, cost + 1))
                visited.append(next_pos)
    return 0