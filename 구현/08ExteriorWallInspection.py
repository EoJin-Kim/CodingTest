from itertools import permutations

def solution(n,weak,dist):
    length = len(weak)
    for i in range(length):
        weak.append(weak[i]+n)

    # 투입할 친구 수의 최솟값을 찾아야 하므로 len(dist)+1
    # 최솟값 min 함수 사용해야 함으로 최대 값보다 1큰수 넣어서 초기화
    answer = len(dist)+1

    #0부터 length-1까지 시작점을 설정
    for start in range(length):

        #친구를 나열하는 모든 순열
        for friends in list(permutations(dist,len(dist))):
            count=1 # 투입할 친구의 수

            #해당 친구가 점검할 수 있는 마지막 위치
            position = weak[start]+friends[count-1]

            # 시작점부터 모든 취약 지점을 확인
            # 원 형태를 2배로 늘렸으므로 start+length 해줘도 상관 없음
            for index in range(start,start+length):
                #점검 범위 벗어나는 경우
                #positon 작업 마지막 위치, week[index] 점검 위치
                if position<weak[index]:
                    count+=1
                    if count > len(dist):
                        break
                    position = weak[index]+friends[count-1]
            answer=min(answer,count)
    if answer>len(dist):
        return -1
    return answer
solution(12,[1,3,4,9,10],[3,5,7])