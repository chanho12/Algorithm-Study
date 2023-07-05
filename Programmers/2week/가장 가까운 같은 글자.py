def solution(s):
    answer = []
    result = []
    for j,i in enumerate(s):
        if i not in result:
            answer.append(-1)
            result.append(i)
        else:  # j = 3 i = 'a' // j = 5 i = 'a'
            
            answer.append(j- s[:j].rfind(i))
    return answer

