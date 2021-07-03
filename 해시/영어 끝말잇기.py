def solution(n, words):
    answer = []
    wordsCount=len(words)
    wordSet=set()
    cnt=1
    turn=1
    last=words[0][0]
    for word in words:
        if cnt>n:
            turn+=1
            cnt=1
        if last[-1] != word[0]:
            break
        length1=len(wordSet)
        wordSet.add(word)
        length2=len(wordSet)
        if length1==length2:
            break
        cnt+=1
        last=word
    #print((turn-1)*n+cnt-1)
    if (turn-1)*n+cnt-1==wordsCount:
        return [0,0]
    return [cnt,turn]

print(solution(3,["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]))
print(solution(5,["hello", "observe", "effect", "take", "either", "recognize", "encourage", "ensure", "establish", "hang", "gather", "refer", "reference", "estimate", "executive"]))
print(solution(2,["hello", "one", "even", "never", "now", "world", "draw"]))