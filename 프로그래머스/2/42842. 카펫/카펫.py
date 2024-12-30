def solution(brown, yellow):
    for x in range(3, brown//2):
        for y in range(3, brown//2):
            if ((2 * x) + (2 * y) - 4 == brown) and ((x - 2) * ( y - 2) == yellow) and (x >= y):
                return [x, y]