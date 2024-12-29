from collections import deque
"""def solution(prices):
    result = [0] * len(prices)
    price = deque((i,v) for i,v in enumerate(prices))
    i = 0
    while True:
            if len(price) == 0: break
            a = price.popleft()
            print(a)
            print(price)
            for q in price:
                if a[1] <= q[1]:
                    result[a[0]] += 1
                    print(result)
    
    return result"""
# for문에서 break를 안넣어줘서 시간초과가 난 듯

def solution(prices):
    queue = deque(prices)
    answer = []
    
    while queue:
        price = queue.popleft()
        sec = 0
        for q in queue:
            sec += 1
            if price > q:
                break 
        answer.append(sec)        
    return answer