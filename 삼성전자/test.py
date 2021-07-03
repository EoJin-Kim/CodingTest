import copy
array=[1,2,3,4]

a=1





def test():

    #array=copy.deepcopy(array)
    #array[0] = 0
    test2(array)
    print(array)
    return 0

def test2(array):
    array[0] = 0

test()
print(array)
print(a)