array=list(input())
changeCount = 0
last="-1"
for i in array:

    if last!=i:
        changeCount+=1
    last=i
print(changeCount//2)