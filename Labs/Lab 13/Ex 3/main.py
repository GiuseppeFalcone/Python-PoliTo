import functions


def printing(p):
    for i in range(len(p)):
        if p[i][0] > 0:
            print('+', end='')
        print(f"{p[i][0]}", end='')
        if p[i][1] != 0:
            print(f"x^{p[i][1]}", end=' ')
    print()


def main():
    print(f"Insert the polynomial\nIf the number has no x, then put 0 when the program asks for the x power\nTp stop inserting values insert -766 in the number")
    finish = True
    p = list()
    while finish:
        num = int(input("Enter a number:"))
        if num == -766:
            finish = False
        else:
            power = int(input("Enter the power of x: "))
            b = (num, power)
            p.append(b)
    p.sort(key = lambda x: x[1], reverse=True)
    printing(p)

    exiting = None
    while exiting != 9:
        exiting = int(input("Select What You want to do:\n1)\tAdd\n2)\tMultiply\n3)\tAdd Term\n9)\tExit"))
        if exiting == 1:
            print("Insert the number and the power to add: ")
            number = int(input("Number: "))
            power = int(input("Power: "))
            p = functions.add(p, number, power)
            printing(p)
        if exiting == 2:
            print("Insert the number and the power to multiply by: ")
            number = int(input("Number: "))
            power = int(input("Power: "))
            p = functions.multiplying(p, number, power)
            printing(p)
        if exiting == 3:
            print("Enter the number and the power of x to add:")
            number = int(input("Number: "))
            power = int(input("Power: "))
            p = functions.add_term(p, number, power)
            printing(p)

    q = functions.mul_q(p)
    printing(q)

if __name__ == '__main__':
    main()
