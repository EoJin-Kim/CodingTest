
def binary_search(oper, some_list,list_len):
    start=0
    end=max(some_list)

    while start<=end:
        result = 0
        mid =(start+end)//2
        for i in some_list:
            if i>mid:
                result+=i-mid

        if oper>result:
            end = mid - 1

        elif oper<result:
            start = mid + 1
        else:
            return mid
    return mid

n,m = map(int,input().split())
data=list(map(int,input().split()))
print(binary_search(m,data,n))