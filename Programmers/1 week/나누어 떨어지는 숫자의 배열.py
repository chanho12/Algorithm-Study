def solution(arr, divisor):
    array = sorted([i for i in arr if i%divisor ==0 ])
    if len(array) == 0:
        answer = [-1]
    else:
        answer = array
    return answer
