def solution(t, p):
    answer = len([int(t[i:i+len(p)]) for i in range(0, len(t) - len(p) + 1) if int(t[i:i+len(p)]) <= int(p)])
    return answer
