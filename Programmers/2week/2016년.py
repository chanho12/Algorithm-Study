def solution(a, b):
    date = ['MON','TUE','WED','THU','FRI','SAT','SUN']
    import datetime as dt
    answer = date[dt.date(2016,a,b).weekday()]
    return answer
