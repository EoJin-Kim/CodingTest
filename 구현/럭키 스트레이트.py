n=input()

result1=0
result2=0
for i in n[:len(n)//2]:
    result1+=int(i)

for i in n[len(n)//2:]:
    result2+=int(i)

if result2==result1:
    print("LUCKY")
else:

    print("READY")