def solution(a, b):
    month_days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    day_of_week = {}
    for day in range(1, 365 + 1):
        if day % 7 == 1:
            day_of_week[day] = 'FRI'
        elif day % 7 == 2:
            day_of_week[day] = 'SAT'
        elif day % 7 == 3:
            day_of_week[day] = 'SUN'
        elif day % 7 == 4:
            day_of_week[day] = 'MON'
        elif day % 7 == 5:
            day_of_week[day] = 'TUE'
        elif day % 7 == 6:
            day_of_week[day] = 'WED'
        elif day % 7 == 0:
            day_of_week[day] = 'THU'

    if a == 1:
        return day_of_week.get(b)
    return day_of_week.get(sum(month_days[:a - 1]) + b)


def other(a, b):
    month_days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    day_of_week = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']
    return day_of_week[((sum(month_days[:a - 1]) + b) % 7 - 1)]


print(solution(5, 24))
print(other(5, 24))
