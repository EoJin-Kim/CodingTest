dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def Direction(s):
    if s == "U":
        direction = 0
    elif s == "R":
        direction = 1
    elif s == "D":
        direction = 2
    else:
        direction = 3
    return direction


def solution(dirs):
    answer = []
    x, y, = 0, 0
    for d in dirs:
        direction = Direction(d)
        nx = x + dx[direction]
        ny = y + dy[direction]
        if nx >= -5 and nx <= 5 and ny >= -5 and ny <= 5:
            if not {(x,y),(nx,ny)} in answer:
                answer.append({(x,y),(nx,ny)})
            x,y=nx,ny

    return len(answer)

print(solution("ULURRDLLU"))