def solution(k, score):
    answer = []
    for i in range(len(score)): # k = 3, range = 0~6
        answer.append(min(sorted(score[:i+1], reverse=True)[:k]))
    return answer
