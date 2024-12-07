def solution(numbers, direction):
    if direction == 'right':
        n = numbers.pop(-1)
        numbers.insert(0,n)
    else:
        n = numbers.pop(0)
        numbers.insert(len(numbers),n)
    return numbers