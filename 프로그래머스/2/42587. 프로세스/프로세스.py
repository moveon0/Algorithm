def solution(priorities, location):
    queue =  [(i,p) for i,p in enumerate(priorities)] #enumerate로 인덱스와 값 저장
    answer = 0
    while True:
        cur = queue.pop(0)                      #맨 앞 요소 
        if any(cur[1] < q[1] for q in queue):   #추출한 요소가 다음 요소보다 작으면 다시 넣음
            queue.append(cur)
        else:
            answer += 1                         #인덱스 증가
            if cur[0] == location:              #추출값이 목표값과 같으면 반환
                return answer
