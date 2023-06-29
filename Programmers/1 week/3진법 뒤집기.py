def solution(n):
    new_list = []
    new_list.append(str(n%3))
    number = n 
    while True: 
        if number // 3 == 0:
            break
        number = number//3  # // 몫 , % 나머지 기호
        new_list.append(str(number%3))
    new_number = int(''.join(new_list))
    k = 0
    sum = 0
    for i in str(new_number)[::-1]:
        i = int(i)
        sum = sum + i * (3**k)
        k = k +1
    answer = sum
    return answer
