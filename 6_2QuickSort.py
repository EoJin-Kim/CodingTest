array=[5,7,9,0,3,1,6,2,4,8]

def quick_sort(array):
    if len(array)<=1:
        return array
    pivot=array[0]
    tail=array[1:]

    leftSide=[x for x in tail if x<=pivot]
    rightSide=[x for x in tail if x>pivot]
    return quick_sort(leftSide)+[pivot]+quick_sort(rightSide)

print(quick_sort(array))
