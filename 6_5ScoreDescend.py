n=int(input())
array=[]
for i in range(n):
    input_data=input().split()
    array.append((input_data[0],int(input_data[1])))

def settings(array):
    return array[1]

result = sorted(array,key=settings,reverse=True)
for i in result:
    print(i[0],end=' ')
