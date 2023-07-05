def solution(food):
    result = ''
    for i,j in enumerate(food[1:]):
        if j%2 == 1:
            number = int((j-1)/2)
            result = result + str(i+1) * number
        else:
            number = int(j/2)
            result = result + number * str(i+1)
    answer = result + '0' + result[::-1]
    return answer
