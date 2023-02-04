def main():
    """Main entry point"""

    # list a
    a = list()
    flag_ = False  # Flag
    print("Now you are inserting the values of the first list \n To exit insert \"-10\"")
    while not flag_:
        x = int(input("Enter a value"))
        if x != -10:    # Checking for exit value
            a.append(x)
        else:
            flag_ = True

    b = list()
    flag_ = False
    print("Now you are inserting the values of the second list \n To exit insert \"-10\"")
    while not flag_:
        x = int(input("Enter a value"))
        if x != -10:
            b.append(x)
        else:
            flag_ = True

    print(a)
    print(b)

    print(merge(a, b))

def merge(a, b):
    c = list()
    for i in range(0, len(a)+len(b), 1):
        if i < len(a):
            c.append(a[i])
        if i < len(b):
            c.append(b[i])
    return c


if __name__ == '__main__':
    main()
