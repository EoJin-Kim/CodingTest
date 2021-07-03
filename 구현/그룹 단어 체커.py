'''

3
happy
new
year

4
aba
abab
abcabc
a
'''


def StrCheck(word):
    setAlpha = set()
    last = ""
    for j in word:
        if last != j:
            length1 = len(setAlpha)
            setAlpha.add(j)
            length2 = len(setAlpha)
            if length1 == length2:
                return False
        last = j
    return True


answer = 0

for i in range(int(input())):
    word = input()
    # word="aba"
    if StrCheck(word):
        answer += 1

print(answer)
