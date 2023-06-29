def solution(s):
    upper_list = sorted([i for i in s if i.isupper()], reverse=True)
    lower_list = sorted([i for i in s if i.islower()],reverse = True)
    answer = ''.join(lower_list+upper_list)
    return answer
