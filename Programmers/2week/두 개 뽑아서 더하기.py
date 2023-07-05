def solution(numbers):
    from itertools import combinations
    answer = sorted(list(set([sum(i) for i in list(combinations(numbers,2))])))
    return answer
