def solution(s):
    stack=[]

    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    for i in s:
        if len(stack)==0:
            if i==")":
                return False
            else:
                stack.append(i)
        else:
            if stack[-1]!=i:
                stack.pop()
                continue
            else:
                stack.append(i)
    if len(stack)==0:
        return True
    else:
        return False