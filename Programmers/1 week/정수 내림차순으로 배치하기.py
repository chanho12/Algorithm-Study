def solution(n):
    number = sorted([i for i in list(str(n))],reverse=True)
    answer = ''.join([str(i) for i in number])
    return int(answer)
