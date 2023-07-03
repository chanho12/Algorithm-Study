def solution(s, n):
    dic = {i : j for i, j in zip('abcdefghijklmnopqrstuvwxyz', range(0,26))}
    dic1 = {j : i for i, j in zip('abcdefghijklmnopqrstuvwxyz', range(0,26))}
    new = []
    for i,j in enumerate(s.lower()):
        if s[i].islower():
            new.append(dic1[(dic[j] + n)%26])
        elif s[i].isupper():
            new.append(dic1[(dic[j] + n)%26].upper())
        else: 
            new.append(' ')
    answer = ''.join(new)
    return answer
