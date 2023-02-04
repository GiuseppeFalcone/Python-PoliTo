str1 = input("Enter a string= ")

if str1.isalpha():
    print("Contains only letters")
    if str1.isupper():
        print("Contains only uppercase latters")
    if str1.islower():
        print("COntains only lowercase letter")

if str1.isdigit():
    print("Contains only digits")

if str1.isalnum():
    print("Contains only letters and numbers")

if str1[0].isupper():
    print("starts with a capital letter")

if str1[-1] == '.':
    print("Ends with a period")