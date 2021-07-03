# print(list(enumerate([1,2,3],start=1)))

array = [False] * 10001
for i in range(1, 10001):
    # i 33
    check = 0
    check += i
    while i != 0:
        check += i % 10
        i = i // 10

    if check > 10000:
        continue
    array[check] = True

for i in range(1, 10001):
    if array[i] == False:
        print(i)
