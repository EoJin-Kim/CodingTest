import sys
#sys.stdin = open('input.txt')



def chese_calc(array,x,y):

    answer1=0
    answer2 = 0
    for i in range(x,x+8):
        for j in range(y,y+8):
            if i%2==0:
                if j%2==0 and array[i][j]=="W":
                    pass
                elif j % 2 == 1 and array[i][j] == "B":
                    pass
                else:
                    answer1+=1
            else:
                if j%2==0 and array[i][j]=="B":
                    pass
                elif j % 2 == 1 and array[i][j] == "W":
                    pass
                else:
                    answer1+=1


    for i in range(x,x+8):
        for j in range(y,y+8):
            if i%2==0:
                if j%2==0 and array[i][j]=="B":
                    pass
                elif j % 2 == 1 and array[i][j] == "W":
                    pass
                else:
                    answer2+=1
            else:
                if j%2==0 and array[i][j]=="W":
                    pass
                elif j % 2 == 1 and array[i][j] == "B":
                    pass
                else:
                    answer2+=1
    return(min(answer2,answer1))
answer=int(1e9)
row,col = map(int,input().split())
array=[input() for i in range(row)]

for i in range(row-7):
    for j in range(col-7):
        answer=min(chese_calc(array,i,j),answer)
print(answer)


# print(answer1)
# print(answer2)
# print(min(answer1,answer2))