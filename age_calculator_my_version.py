# Given your birthday and the current date, calculate your age
# in days. Compensate for leap days. Assume that the birthday
# and current date are correct dates (and no time travel).
# Simply put, if you were born 1 Jan 2012 and todays date is
# 2 Jan 2012 you are 1 day old.

# IMPORTANT: You don't need to solve the problem yet!
# Just brainstorm ways you might approach it!

daysOfMonths = [ 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def isLeapYear(year):
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True

def daysBetweenDates(y1, m1, d1, y2, m2, d2):
    years = (y1 - y2) - 1
    leapYears=0
    days_of_current_year = 0
    days_of_birth_year = 0
    for i in range(y2, y1):
        if isLeapYear(i):
            leapYears+=1
    for i in range(0,m1-1):
        days_of_current_year += daysOfMonths[i]
    for i in range(m2, 12):
        days_of_birth_year += daysOfMonths[i]
    days_in_birth_month = daysOfMonths[d2-1] - d2

    days = (years * 365) + (leapYears-1) + days_of_current_year + days_of_birth_year + days_in_birth_month + d1
    return days

print daysBetweenDates(2018,1,30,1980,10,12)
