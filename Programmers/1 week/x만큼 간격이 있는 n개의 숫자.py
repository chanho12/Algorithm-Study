def solution(x, n):
    if x < 0:
        answer = [i for i in range(x, x*n-1, x)]
    elif x > 0:
        answer = [i for i in range(x, x*n+1 ,x)]
    else:
        answer= [int(i) for i in '0'*n]
    return answer
