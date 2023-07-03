def solution(sizes):
    w = []
    h = []
    for z in sizes:
        w.append(max(z))
        h.append(min(z))
    answer = max(w) * max(h)
    return answer
