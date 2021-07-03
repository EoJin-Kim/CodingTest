from itertools import permutations
import copy
from collections import deque

def solution(expression):
    # +, -, *
    #[0, 1, 2]
    answer = 0

    exp=[]
    array=[]
    temp=""
    for i in expression:
        if i=="+" or i=="-" or i=="*":
            exp.append(i)
            array.append(temp)
            temp=""
            continue
        temp+=i

    if temp:
        array.append(temp)

    array = list(map(int, array))
    maxValue=0

    for i in permutations(["+","-","*"],3):
        value = abs(CalcValue(array,exp,i))
        if value>maxValue:
            maxValue=value
        print(i)
    print(array)
    print(exp)

    return maxValue
def CalcValue(numbers,ep,seq):
    numbers=copy.deepcopy(numbers)
    ep=copy.deepcopy(ep)
    for i in seq:
        k=0
        while True:
            if k >=len(ep):
               break
            if ep[k]==i:
                if ep[k]=="+":
                    numbers[k]=numbers[k]+numbers[k+1]
                    numbers.pop(k+1)
                    ep.pop(k)
                    continue
                elif ep[k]=="-":
                    numbers[k]=numbers[k]-numbers[k+1]
                    numbers.pop(k+1)
                    ep.pop(k)
                    continue
                else:
                    numbers[k]=numbers[k]*numbers[k+1]
                    numbers.pop(k+1)
                    ep.pop(k)
                    continue
            k+=1

    return numbers[0]

print(solution("100-200*300-500+20"))