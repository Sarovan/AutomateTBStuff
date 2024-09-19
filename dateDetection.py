import re, sys

text = "29/02/4444"
months30 = (4, 6, 9, 11)


def date_assessor(day, month, year):
    leapYear = False
    if year % 4 == 0:
        if year % 100 == 0 and year % 400 != 0:
            pass
        else:
            leapYear = True
    if month in months30 and day > 30:
        return False
    elif month == 2 and ((leapYear and day > 29) or (not leapYear and day > 28)):
        return False
    else:
        return True


date_result = re.compile(r"([0-2]\d|[3][0-1])\/([0]\d|[1][0-2])\/([1-2]\d{3})")
date = date_result.search(text)

try:
    day = int(date.group(1))
    month = int(date.group(2))
    year = int(date.group(3))
except AttributeError:
    print("Date entry incorrect!")
    sys.exit()

if date_assessor(day, month, year):
    print("Date is valid.")
else:
    print("Date is invalid!")
