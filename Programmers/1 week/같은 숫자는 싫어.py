def solution(arr)
    number = []
    for i in range(0,len(arr)-1):
        if arr[i] == arr[i+1]:
            number.append((arr[i],i))
    new_list = list(range(0, len(arr)))
    for i,j in number:
        try:
            new_list.remove(i)
        except:
            pass
    answer = [a[i] for i in new_list]
    return answer
