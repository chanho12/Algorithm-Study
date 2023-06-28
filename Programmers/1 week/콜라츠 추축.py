def solution(num):
    rotation = 0
    while True:
        if num%2 == 0:
            num = num/2
            rotation = rotation + 1
	elif num == 1:
	    rotation = 0
	    break
        else:
            num = (num * 3) + 1
            rotation = rotation + 1
        if num == 1:
            break
        elif rotation >=500:
            rotation = -1
            break
    answer = rotation
    return answer
