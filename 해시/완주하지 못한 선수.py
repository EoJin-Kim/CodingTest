from collections import Counter

def solution(participant, completion):
    participantCounter = Counter(participant)
    completionCounter = Counter(completion)
    completion=set(completion)
    for key,value in participantCounter.items():
        #print(completionCounter.get(key))
        if not completionCounter[key]:
            return key
        else:
            if completionCounter[key] !=participantCounter[key]:
                return key


print(solution(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"]))