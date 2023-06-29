def solution(s):
    answer = True
    if len(s) != 4 and len(s) != 6:
        answer = False
    number = [i for i in s if i.isdigit()]
    if len(number) != len(s):
        answer = False
    return answer
