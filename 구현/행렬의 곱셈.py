def solution(arr1, arr2):
    row = len(arr1)
    col = len(arr1[0])

    #answer = [[0 for i in range(col)] for j in range(row)]
    answer = [[0 for _ in range(len(arr2[0]))] for _ in range(len(arr1))]
    for i in range(len(arr1)):
        for j in range(len(arr2[0])):
            for k in range(len(arr1[0])):
                answer[i][j] += (arr1[i][k] * arr2[k][j])
    #print(answer)
    return answer


print(solution([[1, 4], [3, 2], [4, 1]],[[3, 3], [3, 3]]))