def solution(s):
    p = s.lower().count('p') 
    y = s.lower().count('y')
    
    if p == y:
        answer = True
    elif p != y:
        answer = False
    return answer
