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
    # 코드를 작성하세요.


def bs(element,someList):
    start=0
    end=len(someList)-1

    while start<=end:
        mid = (end - start) // 2
        if someList[mid]==element:
            return mid
        elif someList[mid]>element:
            end=mid-1
        else:
            start = mid +1


print(binary_search(2, [2, 3, 5, 7, 11]))
print(binary_search(0, [2, 3, 5, 7, 11]))
print(binary_search(5, [2, 3, 5, 7, 11]))
print(binary_search(3, [2, 3, 5, 7, 11]))
print(binary_search(11, [2, 3, 5, 7, 11]))

print(bs(2, [2, 3, 5, 7, 11]))