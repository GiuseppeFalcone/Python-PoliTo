#Input times
print("Enter your two appointment starting and end hours\n-First appointment ")
start_1 = int(input("Starting time: "))
end_1 = int(input("Ending time: "))

print("-Second appointment")
start_2 = int(input("Starting time: "))
end_2 = int(input("Ending time: "))

#Checking the times
if start_1 > start_2 :
    s = start_1
else:
        s = start_2

if end_1 < end_2 :
    e = end_1
else:
        e = end_2

if s < e :
    print("The appointments overlap")
else:
        print("The appointments don't overlap")
