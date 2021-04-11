import sys
n = int(input())
array = set(map(int,sys.stdin.readline().rstrip().split()))

m = int(input())
demand = list(map(int,sys.stdin.readline().rstrip().split()))
print(array)
for i in demand:
    if i in array:
        print("yes",end=" ")
    else:
        print("no",end=" ")