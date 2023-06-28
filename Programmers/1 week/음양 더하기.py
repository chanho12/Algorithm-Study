def solution(absolutes, signs):
    sum = 0
    for i,j in zip(absolutes, signs):
        if j == True:
            sum = sum+i
        else:
            sum = sum - i
    answer = sum
    return answer
