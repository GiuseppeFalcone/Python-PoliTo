day = int(input("What day of the month is it? (Please express it in number):"))
month = int(input("What month is it? (Please express it in number): "))
if month == 1 or 2 or 3:
    season = "Winter"
elif month == 4 or 5 or 6:
    season = "Spring"
elif month == 7 or 8 or 9:
    season = "Summer"
elif month == 10 or 11 or 12:
    season = "Fall"

print(season)

if month % 3 == 0 and day >= 21:
    if season == "Winter":
        season = "Spring"
    elif season == "Spring":
        season = "Summer"
    elif season == "Summer":
        season = "Fall"
    else:
        season = "Winter"
print(season)

