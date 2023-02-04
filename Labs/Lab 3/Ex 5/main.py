year = int(input("Enter the year "))

is_leap = False
if year % 4 == 0:
    is_leap = True
    if year % 100 == 0:
        is_leap = False
        if year % 400 == 0:
            is_leap = True

print(is_leap)

print(f"Year {year} is{'' if is_leap else ' NOT '}a leap year")