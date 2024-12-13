

    
def solution(participant, completion):

    name_count = {}


    ### name_count[name] = name_count.get(name, 0) + 1와 name_count[name] += 1의 차이는 name_count 딕셔너리에 해당 키(name)가 존재하지 않을 때 발생합니다. ###

    for name in participant:
        name_count[name] = name_count.get(name,0) + 1

    for name in completion:
        name_count[name] -= 1

    for name, count in name_count.items():
        if count != 0:
            return name