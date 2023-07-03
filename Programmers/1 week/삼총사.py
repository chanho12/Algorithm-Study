def solution(number):
    from itertools import combinations
    answer = len([i for i in list(combinations(number,3)) if sum(i) == 0 ])
    return answer
