N = int(input("Number of friends"))
bill = float(input("Bill amount "))

tip_percentage = 15
#processing

tip = tip_percentage/100*bill
total = bill+tip

total_per_person = total/(N+1)
bill_per_person = bill/(N+1)
tip_per_person = tip/(N+1)

#output
print("The bill is: ", bill)
print("The tip is: ", tip)
print("The total amount is: ",  total)
print("The total per person", total_per_person)
print("The bill per person is: ", bill_per_person)
print("The tip per person is: ", tip_per_person)