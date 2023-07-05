def solution(a,b,n):
    answer = 0
    while a <= n:
        i,j = divmod(n,a)
        answer += i*b
        n = j + i*b
    return answer
