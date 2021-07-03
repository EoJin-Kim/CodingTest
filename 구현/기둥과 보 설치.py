def solution(n, build_frame):
    answer = []

    for oper in build_frame:
        x,y,a,b=oper

        #설치
        if b==1:
            answer.append([x,y,a])
            #빌드가 안되면
            if BuildCheck(answer)==False:
                # 다시 삭제
                answer.remove([x,y,a])

        # 삭제
        else:
            answer.remove([x, y, a])
            # 빌드가 안되면
            if BuildCheck(answer)==False:
                answer.append([x,y,a])
        # 다시 설치
    answer.sort()
    return answer

def BuildCheck(answer):
    for x,y,case in answer:
        # 기둥 일 경우
        if case== 0:
            if y== 0 or [x-1,y,1] in answer or [x,y-1,0] in answer or [x,y,1] in answer:
                continue
            else:
                return False
        # 보 일 경우
        elif case==1:
            if [x,y-1,0] in answer or [x+1,y-1,0] in answer or [x-1,y,1] in answer and [x+1,y,1] in answer:


                continue
            else:
                return False

    return True



#print(solution(5,[[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]))
print(solution(5,[[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]))