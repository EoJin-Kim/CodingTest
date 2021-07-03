from bisect import bisect_left,bisect_right


def NumCount(left,right):
        leftIndex = bisect_left(data,left)
        rightIndex = bisect_right(data,right)
        return rightIndex-leftIndex

n,x = map(int,input().split())
data=list(map(int,input().split()))
print(NumCount(x,x))

'''
7 2
1 1 2 2 2 2 3

7 4
1 1 2 2 2 2 3 

'''