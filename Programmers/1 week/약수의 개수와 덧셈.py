def solution(left, right):
    sum = 0
    for p in range(left, right+1):
        number = [i for i in range(1, p+1) if p%i == 0]
        if len(number) %2 == 0:
            sum = sum + p
        else:
            sum = sum- p
    answer = sum
    return answer
