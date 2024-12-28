from collections import deque # deque 내장함수가 pop보다 효율성이 더 좋다.

def solution(bridge_length, weight, truck_weights):
    
    time = 0
    bridge = deque([0] * bridge_length)  # [0]*bridge_length 을 덱으로 변환
    truck_weights = deque(truck_weights) # 리스트를 덱으로 변환
    
    currentWeight = 0                    # 다리의 현재 무게
    while len(truck_weights) > 0:
        time = time + 1                  # 다리에 트럭이 올라갈 때마다 시간 +1

        currentWeight = currentWeight - bridge.popleft()    #트럭이 다리에서 내리면 현재 무게 감소

        if currentWeight + truck_weights[0] <= weight:      
            currentWeight = currentWeight + truck_weights[0]
            bridge.append(truck_weights.popleft())

        else: 
            bridge.append(0)
            
    time = time + bridge_length         #마지막 트럭이 다리를 건너는 시간
    
    return time
# 이해 안되는 점 bridge_length가 100 인데 버티는 무게가 10이면 안되지 않나..