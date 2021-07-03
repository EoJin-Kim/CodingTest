def binary_search(element, some_list):
    start=0
    end=len(some_list)-1
    while start<=end:
        mid =(start+end)//2
        if element>some_list[mid]:
            start=mid+1
        elif element<some_list[mid]:
            end=mid -1
        else:
            return mid
    return


n=int(input())
array=list(map(int,input().split()))
k=int(input())
data=list(map(int,input().split()))

for i in data:
    if binary_search(i,array):
        print("yes",end=" ")
    else:
        print("no",end=" ")