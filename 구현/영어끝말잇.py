def solution(n, words):
    answer = []
    wordsCount=len(words)
    wordSet=set()
    cnt=1
    turn=1
    last=words.pop(0)
    wordSet.add(last)
    check=True
    for word in words:

        if last[-1] != word[0] or word in wordSet:
            cnt+=1
            check=False
            break

        wordSet.add(word)
        cnt+=1
        last=word
        if cnt==n:
            turn+=1
            cnt=0

    if check:
        return [0,0]
    else:
        return [cnt,turn]


print(solution(3,["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]))
print(solution(5,["hello", "observe", "effect", "take", "either", "recognize", "encourage", "ensure", "establish", "hang", "gather", "refer", "reference", "estimate", "executive"]))