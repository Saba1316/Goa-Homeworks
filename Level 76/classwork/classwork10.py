# Codewars 7 kyu: Unlucky Days

from datetime import datetime, date

def unlucky_days(year):
    return sum(date(year, m, 13).weekday() == 4 for m in range(1, 13))