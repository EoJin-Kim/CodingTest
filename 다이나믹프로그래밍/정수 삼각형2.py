def solution(triangle):
    answer = 0
    size=len(triangle)
    for i in range(1,size):
        for j in range(len(triangle[i])):
            if j==0:
                left_up=0
                right_up=triangle[i-1][j]

            elif j==len(triangle[i])-1:
                left_up=triangle[i-1][j-1]
                right_up=0
            else:
                left_up = triangle[i - 1][j - 1]
                right_up = triangle[i - 1][j]
            triangle[i][j]=triangle[i][j]+max(left_up,right_up)



    return max(triangle[-1])

print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))
'''
7
3 8
8 1 0
2 7 4 4
4 5 2 6 5
'''