import copy
def solution(key, lock):
    keyLen=len(key)
    lockLen = len(lock)
    plane = [ [0] * (2*keyLen + lockLen) for _ in range(2*keyLen + lockLen)]

    for i in range(len(lock)):
        for j in range(len(lock[0])):
            plane[keyLen+i][keyLen+j] = lock[i][j]


    # 바닥 확인
    #for i in plane:
    #    print(i)
    check=False
    planeLen = len(plane)
    #회전 4번 주기
    for _ in range(4):
        for i in range(planeLen-keyLen+1):
            for j in range(planeLen-keyLen+1):
                planeDup = copy.deepcopy(plane)
                for z in range(keyLen):
                    for x in range(keyLen):
                        print(i,j,z,x)
                        planeDup[i+z][j+x] +=key[z][x]

                for low in planeDup:
                    print(low)
                print("------------------------")
                result = CheckKey(keyLen,lockLen,planeDup)
                if result:
                    return result




        key=Rotate90(key)
    return result


def Rotate90(a):
    n=len(a)
    m=len(a[0])
    result = [[0]*n for _ in range(m)]
    for i in range(n):
        for j in range(m):
            result[j][n-i-1] = a[i][j]
    return result

def CheckKey(keyLen,lockLen,planeDup):
    for i in range(keyLen, keyLen + lockLen):
        for j in range(keyLen, keyLen + lockLen):
            if planeDup[i][j] != 1:
                return False
    return True

if solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]],[[1, 1, 1], [1, 1, 0], [1, 0, 1]]):
    print("true")
else:
    print("false")