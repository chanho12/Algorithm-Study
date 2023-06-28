def solution(x):
    number = sum([int(i) for i in str(x)])
    if x % number == 0:
        answer = True
    else:
        answer = False
    
    return answer
