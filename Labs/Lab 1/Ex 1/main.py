#inputs: start, end, workdays, distance

start =float(input("Enter the start mileage: "))
end =float(input("Enter the end mileage: "))
workdays = int(input("Enter the working days: "))
distance = float(input("Enter the home-work distance: "))

#processing part
work_mileage = 2*distance*workdays
total=end-start
personal_mileage = total-work_mileage

#outputs
work = work_mileage/total
personal = personal_mileage/total #1-work

print("The fraction for commuting to work is: ", work)
print("The fraction for personal use is: ", personal)