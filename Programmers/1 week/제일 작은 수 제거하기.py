def solution(arr):
    if len(arr) == 1:
        arr.remove(min(arr))
        arr.insert(0,-1)
        return arr
    else:
        arr.remove(min(arr))
        return arr