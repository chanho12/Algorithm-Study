def solution(name, yearning, photo):
    answer = []
    for i in photo:
        number = []
        for j in i:
            if j in name:
                number.append(yearning[name.index(j)])
        answer.append(sum(number))        
    
    return answer
