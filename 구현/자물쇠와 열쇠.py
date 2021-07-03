def solution(key, lock):
    length=len(lock)

    plane=[[0] *(length*3) for _ in range(length*3)]

    for i in range(length):
        for j in range(length):
            plane[length+i][length+j]=lock[i][j]

    for i in range(length*2):
        for j in range(length*2):
            for turn in range(4):
                key=Rotate90(key)

                for x in range(len(key)):
                    for y in range(len(key)):
                        plane[i+x][j+y] += key[x][y]

                if planeCheck(plane):
                    return True

                for x in range(len(key)):
                    for y in range(len(key[0])):
                        plane[i+x][j+y] -= key[x][y]

    print(plane)
    return False

def planeCheck(plane):
    result=True
    lock_len = len(plane)//3
    for i in range(lock_len,lock_len*2):
        for j in range(lock_len,lock_len*2):
            if plane[i][j]!=1:
                return False
    return True

def Rotate90(a):
    n=len(a)
    m=len(a[0])
    result = [[0]*n for _ in range(m)]
    for i in range(n):
        for j in range(m):
            result[j][n-i-1] = a[i][j]
    return result


print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]],[[1, 1, 1], [1, 1, 0], [1, 0, 1]]))