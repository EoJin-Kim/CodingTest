import sys

N, M, B = map(int, sys.stdin.readline().split())

List = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
#result = (21470000000, 0)
ans = 21470000000
height = 0
for i in range(257):

    inven = B
    sec = 0

    for j in range(N):
        for k in range(M):
            if List[j][k] > i:
                sec += (List[j][k] - i) * 2
                inven += (List[j][k] - i)
            else:
                sec += (i - List[j][k])
                inven -= (i - List[j][k])
    if inven >= 0:
        if ans >= sec:
            ans = sec
            height = i
    else:
        break

print(ans, height)