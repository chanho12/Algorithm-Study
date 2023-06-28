def solution(numbers):
    sum = 0
    for i in list('1234567890'):
        if int(i) not in numbers:
            sum = sum + int(i)
    return sum
