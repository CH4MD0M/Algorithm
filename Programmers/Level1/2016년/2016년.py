# datetime 모듈 사용
import datetime
def solution(a, b):
    date = datetime.datetime(2016, a, b)
    return date.strftime("%a").upper())

# 일반적인 알고리즘 사용
def solution(a, b):
    months = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    days = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']
    return days[(sum(months[:a - 1]) + b - 1) % 7]