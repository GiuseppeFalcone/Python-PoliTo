def main():
    SIZE = 4

    magic_sqr = list()
    for i in range(SIZE):
        l = list()
        for j in range(SIZE):
            l.append(int(input(f"Enter the value in the position: [{i}][{j}]")))
        magic_sqr.append(l)

    print_matrix(magic_sqr, SIZE)

    if check_magic(magic_sqr, SIZE):
        print(f"The square ->\n{print_matrix(magic_sqr, SIZE)}\n is a MAGIC SQUARE")
    else:
        print(f"The square ->\n{print_matrix(magic_sqr, SIZE)}\n is NOT a MAGIC SQUARE")


def print_matrix(t, SIZE):
    for i in range(SIZE):
        for j in range(SIZE):
            print("| ", end="")
            print(t[i][j], end=" | ")
        print("")


def check_magic(t, SIZE):
    sum_row0 = sum_row1 = sum_row2 = sum_row3 = 0
    sum_col0 = sum_col1 = sum_col2 = sum_col3 = 0
    sum_diag1 = sum_diag2 = 0
    for i in range(SIZE):
        for j in range(SIZE):
            if i == 0:
                sum_row0 += t[i][j]
            if i == 1:
                sum_row1 += t[i][j]
            if i == 2:
                sum_row2 += t[i][j]
            if i == 3:
                sum_row3 += t[i][j]
    if sum_row0 != sum_row1:
        return False
    elif sum_row0 == sum_row1 == sum_row2 == sum_row3:
        for j in range(SIZE):
            for i in range(SIZE):
                if i == 0:
                    sum_col0 += t[i][j]
                if i == 1:
                    sum_col1 += t[i][j]
                if i == 2:
                    sum_col2 += t[i][j]
                if i == 3:
                    sum_col3 += t[i][j]
        if sum_col0 != sum_col1:
            return False
        elif sum_col0 == sum_col1 == sum_col2 == sum_col3:
            for i, j in range(4):
                sum_diag1 += t[i][j]
            for i, j in range(SIZE-1, 0, -1):
                sum_diag2 += t[i][j]
            if sum_diag1 != sum_diag2:
                return False
            elif sum_diag1 == sum_diag2:
                return True


if __name__ == '__main__':
    main()
