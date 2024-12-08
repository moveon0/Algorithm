def solution(l, r):
    answer = []
    
    for i in range(l, r + 1):
        a = 0
        w = list(str(i))
        if w[0] != '5' or i % 5 != 0:
            continue;
        for j in w:
            if j != '5' and j != '0':
                a = 1
                break;
        if a == 0 :
            answer.append(i)
    if len(answer) == 0:
        answer.append(-1)
    return answer