def solution(arr1, arr2):
    arr3 = []
    for i,j in zip(arr1, arr2):
        arr3.append([k+v for k,v in zip(i,j)]) 
    return arr3
