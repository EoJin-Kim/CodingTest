
def Find1Second(myTime,myTimes):
    count = 0
    start = myTime
    end =myTime+1000
    for mtStart,mtEnd in myTimes:
        if mtEnd>=start and mtStart<end:
            count+=1
    return count

def solution(lines):
    maxCount = 0
    myTimes=[]
    for line in lines:
        ymd,hms,duration = line.split()
        hour,minute,second=hms.split(":")
        hour,minute=int(hour),int(minute)
        second=float(second)
        duration = float(duration[:-1])*1000
        end=(hour*3600 + minute* 60 + second)*1000
        start=end-duration+1
        myTimes.append([start,end])

    for myTime in myTimes:
        # 현재 최대 카운트, 리스트 중 하나 start부터 1초 동안 카운트, 리스트 중 하나 end부터 1초 동안 카운트 중 가장 큰 값이 1초중에 가장 많은 연결 수
        maxCount=max(maxCount,Find1Second(myTime[0],myTimes),Find1Second(myTime[1],myTimes))

    return maxCount


print(solution( [
"2016-09-15 20:59:57.421 0.351s",
"2016-09-15 20:59:58.233 1.181s",
"2016-09-15 20:59:58.299 0.8s",
"2016-09-15 20:59:58.688 1.041s",
"2016-09-15 20:59:59.591 1.412s",
"2016-09-15 21:00:00.464 1.466s",
"2016-09-15 21:00:00.741 1.581s",
"2016-09-15 21:00:00.748 2.31s",
"2016-09-15 21:00:00.966 0.381s",
"2016-09-15 21:00:02.066 2.62s"]))