def main():
    """Main Entry Point"""

    size = int(input("Enter the size of the table: "))
    t = list()
    for i in range(size):
        l = list()
        for x in range(size):
            num = int(input(f"Enter the value in the position [{i}][{x}]"))
            l.append(num)
        t.append(l)
    print("Here's the table you created")
    print_matrix(t)

    print("Enter the values of: ")
    row = int(input("Row: "))
    column = int(input("Column: "))
    while 0 <= row <= size and 0 <= column <= size:
        print(f"The neighbour average is {neighbour_average(t, row, column)}")
        row = int(input("row: "))
        column = int(input("column: "))

    if not (0 <= row <= size and 0 <= column <= size):
        print("Row and columns have to be between 0 and the size - 1\n(ex: size = 3 -> Row = 2 | Column = 0)")

def print_matrix(t):
    for i in range(len(t)):
        for j in range(len(t)):
            print("| ", end="")
            print(t[i][j], end=" | ")
        print("")

def neighbour_average(values, row, column):
    t = tot = 0
    lr = list()
    for i in range(row-1, row+2):
        if 0 <= i < len(values):
            lr.append(i)
    lc = list()
    for i in range(column-1, column+2):
        if 0 <= i < len(values[row]):
            lc.append(i)
    for i in lr:
        for j in lc:
            tot += values[i][j]
            t += 1
    if t == 0:
        print("Invalid Position")
        exit()
    return tot/2

if __name__ == '__main__':
    main()