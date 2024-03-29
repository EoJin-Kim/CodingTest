start = ["(", "{", "[", "<"]
end = [")", "}", "]", ">"]

def solution(inputString):
    answer = 0
    k=0
    array=[]
    for i in range(len(inputString)):
        if i==0 and inputString[i] in end:
            return 0

        if inputString[i] in start:
            array.append(inputString[i])
        if inputString[i] in end:
            if checkPos(array[-1],inputString[i]):
                answer+=1
                array.pop()
            else:
                return -(i)
        k+=1
    if array:
        return -(k-1)
    return answer


def checkPos(srt,ed):
    for i in range(4):
        if start[i]==srt:
            a=i
            break
    for j in range(4):
        if end[j]==ed:
            b=j
            break
    if a==b:
        return True
    else:
        return False

print(solution("line [({<plus>})]"))
'''
문제 설명
우리는 일상에서 순서를 표현하거나 부가 정보를 제공하거나 특정 내용을 부각하는 등의 용도로 괄호를 사용합니다. 괄호는 여는 괄호와 닫는 괄호가 한 묶음을 이루어야 한다는 특징이 있으며 다양한 형태가 존재합니다.

아래 규칙에 맞춰 임의의 문자열에서 다양한 괄호를 올바르게 사용했는지 확인할 수 있는 해결법을 제시해 봅시다.

제한 사항
임의의 문자열 inputString이 입력됩니다

공백으로만 이루어진 문자열은 입력되지 않습니다
입력 문자열의 길이는 1 이상입니다
최대 길이는 명시되지 않습니다
괄호는 아래와 같이 네 종류가 있다고 가정합니다
( ), { }, [ ], < >
동일한 형태의 괄호가 여러 번 사용될 수 있습니다.
괄호를 정상적으로 사용했는지 검증한 결과를 반환합니다

인덱스는 0부터 시작합니다.
여닫는 괄호의 짝이 맞지 않으면 닫는 괄호의 인덱스를 음수로 반환합니다.
예를 들어 'line [({<plus>)}]' 경우 14번째 괄호가 짝이 맞지 않기 때문에 인덱스 14의 음수인 -14를 반환합니다.
괄호가 열려 있는 상태로 문자열이 끝나면 문자열의 마지막 인덱스를 음수로 반환합니다.
예를 들어 'line [({<plus>})' 문자열은 괄호 1개가 닫히지 않고 끝나기 때문에 마지막 인덱스 15의 음수인 -15를 반환합니다.
답이 중복으로 존재하는 경우 문자열 왼쪽 기준으로 먼저 등장하는 것을 답으로 합니다.
예를 들어 'ABC({ABC)ABC'의 경우에는 짝이 맞지 않는 괄호와 닫히지 않은 괄호가 동시에 존재하며 이때 왼쪽 기준으로 우선인 -8이 정답이 됩니다.
모든 괄호를 정상적으로 사용했다면 총 괄호 쌍의 개수를 반환합니다.
예를 들어 '(A)[B]'라는 문자열은 2개의 괄호 쌍이 존재하기 때문에 2를 반환합니다.
첫 번째 문자가 닫는 괄호이거나 괄호가 없는 경우에는 0을 반환합니다.
두 번째 문자 이후에서 닫는 괄호가 먼저 나오는 경우에는 닫는 괄호의 인덱스를 음수로 반환합니다.
예를 들어 'ABC)ABC'의 경우에는 -3을 반환합니다.

inputString	result
Hello, world!	0
line [({<plus>)}]	-14
line [({<plus>})	-15
>_<	0
x * (y + z) ^ 2 = ?	1

'''