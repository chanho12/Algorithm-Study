def solution(strings, n):
    number = []
    for i,j in enumerate(strings):
        number.append((j[n],i,j))
    answer = [strings[i[1]] for i in sorted(number, key=lambda x : (x[0], x[2], x[1]))]
    
    return answer
### u 0 e 1 a 2 
