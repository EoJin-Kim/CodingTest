def solution(skill, skill_trees):
    answer = 0
    for skill_tree in skill_trees:
        if SkillCheck(skill, skill_tree):
            answer += 1
    return answer


def SkillCheck(skill, skill_tree):
    order=[]
    for x in skill:
        check = False
        for a in range(len(skill_tree)):
            if skill_tree[a]!=x:
                continue
            if not order:
                order.append((a, skill_tree[a]))
            else:
                if order[-1][0]>a:
                    return False
                order.append((a,skill_tree[a]))
            check=True
            break
        if check==False:
            order.append((99,x))
    return True


print(solution("CBD",["CED"]))