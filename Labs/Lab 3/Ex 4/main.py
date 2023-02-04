month = int(input("Enter the month: "))
day = int(input("Enter the day: "))

if month in range (1, 4):
    season = "Winter"
elif month in range (4, 7):
    season = "Spring"
elif month in range (7, 10):
    season = "Summer"
elif month in range (10, 13):
    season = "Fall"
else:
    print("MOnth is unvalid")
    exit(0)

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