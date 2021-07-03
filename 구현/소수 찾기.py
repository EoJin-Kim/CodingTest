import math
from itertools import permutations
def solution(numbers):

    answer = set()
    length=len(numbers)
    for i in range(1,length+1):
        for j in permutations(numbers,i):
            num=int("".join(j))
            if PnumCheck(num):
                answer.add(num)
    return len(answer)

def PnumCheck(num):
    if num==1 or num==0:
        return False
    for i in range(2,int(math.sqrt(num))+1):
        if num%i==0:
            return False
    return True

print(solution("17"))
print(solution("011"))