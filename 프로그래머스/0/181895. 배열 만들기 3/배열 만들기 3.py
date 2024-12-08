def solution(arr, intervals):
    answer = []
    li1 = arr[intervals[0][0]:intervals[0][1] + 1]
    li2 = arr[intervals[1][0]:intervals[1][1] + 1]
    answer = li1 + li2
    return answer