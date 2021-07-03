def binary_search(element, some_list):
    start=0
    end=len(some_list)-1
    while start<=end:
        mid =(start+end)//2
        if element>some_list[mid][0]:
            start=mid+1
        elif element<some_list[mid][0]:
            end=mid -1
        else:
            return mid
    return

def solution(array):
    answer = []
    length=len(array)
    temp=[]
    for i in range(len(array)):
        temp.append((array[i],i))
    temp.sort()
    #print(temp)
    for a in array:
        pos =binary_search(a,temp)
        pos_idx=temp[pos][1]
        if pos==length-1:
            answer.append(-1)
        else:
            minValue=1000001
            idx=[]
            for i in range(pos+1,length):
                if abs(temp[i][1]-pos_idx)<minValue:
                    idx=[temp[i]]
                    minValue=abs(temp[i][1]-pos_idx)
                elif abs(temp[i][1]-pos_idx)==minValue:
                    idx.append(temp[i])
            '''
            if len(idx)==1:
                answer.append(idx[0][1])
            else:
                print(idx,"--")
                
                '''
            answer.append(sorted(idx, key=lambda x: x[1])[0][1])
            #answer.append(idx[0][1])
            #print(idx)




    return answer


print(solution(	[3, 5, 4, 1, 2]))


배열이 하나 입력됩니다. 배열의 각 원소에 대해 해당 원소의 값보다 큰 원소들 중에서 해당 원소와 가장 가까운 위치에 있는 원소의 인덱스를 찾아주세요.

조건:

특정 원소에 대해, 해당 원소보다 큰 원소가 없다면 -1을 정답으로 합니다.
가장 가까운 원소가 하나 이상이라면, 인덱스가 가장 작은 것을 정답으로 합니다.
각 원소는 0과 100,000 사이의 값입니다.
입력 배열의 길이는 0부터 100,000 사이입니다.
인덱스는 0부터 시작합니다.
이 문제에는 알고리즘의 효율성을 측정하기 위한 테스트 케이스가 포함되어 있으며, 모든 테스트 케이스를 통과하려면 시간복잡도 O(n) 또는 그것보다 효과적인 알고리즘이 필요합니다.
아래 배열을 예시로 확인해 봅시다.

[3, 5, 4, 1, 2]
가장 왼쪽 원소부터 살펴보겠습니다.
3보다 큰 원소 중 가장 가까운 원소는 5이고, 정답은 1.
5보다 큰 원소는 없으므로 정답은 -1.
4보다 큰 원소 중 가장 가까운 원소는 5이므로, 정답은 1.
1보다 큰 원소 중 가장 가까운 원소는 4, 2이고 인덱스는 각각 2, 4입니다. 작은 인덱스를 선택해야 하므로 정답은 2.
2보다 큰 원소 중 가장 가까운 원소는 4이고, 정답은 2.

따라서 정답 배열은 [1, -1, 1, 2, 2]입니다.

입력값 〉	[3, 5, 4, 1, 2]
기댓값 〉	[1, -1, 1, 2, 2]
실행 결과 〉	테스트를 통과하였습니다.
출력 〉	[1, -1, 1, 2, 2]
테스트 2
입력값 〉	[1, 2, 3, 4, 5]
기댓값 〉	[1, 2, 3, 4, -1]
실행 결과 〉	테스트를 통과하였습니다.
출력 〉	[1, -1, 1, 2, 2]
테스트 3
입력값 〉	[7, 4, 4, 2, 9, 6]
기댓값 〉	[4, 0, 0, 2, -1, 4]
실행 결과 〉	테스트를 통과하였습니다.
출력 〉	[1, -1, 1, 2, 2]