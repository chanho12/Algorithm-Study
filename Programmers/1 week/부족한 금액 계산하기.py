def solution(price, money, count):
    full = sum([i for i in range(price,price*count+1,price)])
    answer = full - money
    if answer < 0:
        answer = 0
    
    return answer
