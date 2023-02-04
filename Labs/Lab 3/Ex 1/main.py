a = int(input("Enter a int number"))
b = int(input("Enter a int number"))
c = int(input("Enter a int number"))

if a < b and b < c:
    print("Increasing")
elif a > b and b > c:
    print("decreasing")
else:
    print("neither")