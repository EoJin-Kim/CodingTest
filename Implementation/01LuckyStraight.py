n = input()
mid = len(n)//2

left=n[:mid]
right=n[mid:]
result1=0
result2=0
for i in left:
    result1+=int(i)

for i in right:
    result2+=int(i)

if result1==result2:
    print("LUCKY")
else:
    print("READY")

