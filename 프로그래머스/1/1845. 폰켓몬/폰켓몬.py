def solution(nums):
    li = [None] * int((len(nums)/2))
    key = [nums[0]]
    li.append(key[0])
    for i in nums:
        if len(key) == len(li) or len(key) == int(len(nums) / 2):
            break
        if i in key:
            continue
        else:
            li.append(i)
            key.append(i)
        
    return len(key)