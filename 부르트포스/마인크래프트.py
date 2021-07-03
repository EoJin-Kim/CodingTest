import sys
input = sys.stdin.readline


row,col,count = map(int,input().split())
floor=[]
for i in range(row):
    floor.append(list(map(int,input().split())))
max_high=max(map(max,floor))
min_value,floor_value=int(1e9),-1
for current in range(max_high+1):

    block=0
    build=0
    remove=0

    for i in range(row):
        for j in range(col):

            # 높이가 같으면 continue
            if floor[i][j]==current:
                continue

            # 높이가 높으면 remove
            elif floor[i][j]>current:
                temp=floor[i][j]-current
                remove+=temp


            # 높이가 낮으면 build
            else:
                temp=current-floor[i][j]
                build+=temp
    if remove+count>=build:
        result = remove * 2+build
        if min_value>=result:
            min_value=result
            floor_value=current
    else:
        break

print(min_value,floor_value)






'''
3 4 99
0 0 0 0
0 0 0 0
0 0 0 1

3 4 1
64 64 64 64
64 64 64 64
64 64 64 63
'''