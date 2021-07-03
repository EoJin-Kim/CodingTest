# 수직 수평 1칸
Ndx = [-1, 0, 1, 0]
Ndy = [0, 1, 0, -1]

# 수직 수평 2칸
Cdx1 = [-2, 0, 2, 0]
Cdy1 = [0, 2, 0, -2]

# 대각선 1칸
Cdx2 = [-1, -1, 1, 1]
Cdy2 = [-1, 1, 1, -1]
def solution(places):
    answer = []


    for place in places:
        persons=[]
        partitions=[]
        for i in range(5):
            for j in range(5):
                if place[i][j]=="P":
                    persons.append((i,j))
                elif places[i][j]=="X":
                    partitions.append((i,j))
        #print(person)
        if CheckPerson(place,persons):
            answer.append(1)
        else:
            answer.append(0)


    return answer

def CheckPerson(place,persons):
    for x, y in persons:
        # 수직 수평 한칸 확인
        for i in range(4):
            nx = x + Ndx[i]
            ny = y + Ndy[i]
            if nx >= 0 and nx < 5 and ny >= 0 and ny < 5:
                if place[nx][ny] == "P":
                    return False

        for i in range(4):
            nx = x + Cdx2[i]
            ny = y + Cdy2[i]
            if nx >= 0 and nx < 5 and ny >= 0 and ny < 5:
                if place[nx][ny]=="P":
                    if i==0:
                        if place[x-1][y]=="O" or place[x][y-1]=="O":
                            return False
                    elif i==1:
                        if place[x - 1][y] == "O" or place[x][y + 1] == "O":
                            return False
                    elif i==2:
                        if place[x + 1][y] == "O" or place[x][y + 1] == "O":
                            return False
                    else:
                        if place[x + 1][y] == "O" or place[x][y - 1] == "O":
                            return False

        for i in range(4):
            nx = x + Cdx1[i]
            ny = y + Cdy1[i]
            if nx >= 0 and nx < 5 and ny >= 0 and ny < 5:
                if place[nx][ny]=="P":
                    if not place[(nx+x)//2][(ny+y)//2]=="X":
                        return False


    return True



print(solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPXX", "OXXXP", "POOXX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]))