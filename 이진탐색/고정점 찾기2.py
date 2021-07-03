
def binary_search(someList):
    start=0
    end=len(someList)-1
    while start<=end:

        mid=(end+start)//2
        if mid>someList[mid]:
            start = mid + 1

        elif mid<someList[mid]:
            end = mid - 1
        else:
            return mid

n=int(input())
data=list(map(int,input().split()))
print(binary_search(data))



'''
5
-15 -6 1 3 7

7
-15 -4 2 8 9 13 15

7
-15 -4 3 8 9 13 -15
'''