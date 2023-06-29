def solution(s):
    final = []
    for i in s.split(" "):
        new = []
        if i == '':
            final.append()
        for number, message in enumerate(i):
            if number % 2 == 0:
                change = message.upper()
            else:
                change = message.lower()
            new.append(change)
        final.append(new)
    answer = ' '.join([''.join(i) for i in final])
    return answer
