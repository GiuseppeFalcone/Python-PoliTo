SEATS = [
    [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],
    [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],
    [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],
    [10, 10, 20, 20, 20, 20, 20, 20, 10, 10],
    [10, 10, 20, 20, 20, 20, 20, 20, 10, 10],
    [10, 10, 20, 20, 20, 20, 20, 20, 10, 10],
    [20, 20, 30, 30, 40, 40, 30, 30, 20, 20],
    [20, 30, 30, 40, 50, 50, 40, 30, 30, 20],
    [30, 40, 50, 50, 50, 50, 50, 50, 40, 30]
]
PRICES = [10, 20, 30, 40, 50]


def position(SEATS):
    r = int(input("Enter the row: "))
    c = int(input("Enter the column: "))
    if SEATS[r][c] != 0:
        print(f"The price is {SEATS[r][c]}\nThanks")
        SEATS[r][c] = 0
    elif SEATS[r][c] == 0:
        error_taken()
    elif r > 9 or c > 10:
        r_c_error()


def price(SEATS, PRICES):
    possible_seats = list()
    price = int(input("Enter a price: "))
    if price in PRICES:
        for i in range(9):
            for j in range(10):
                if SEATS[i][j] == price:
                    possible_seats.append((i, j))
        print(f"The possible seats of {price}$ are: \n{possible_seats}\n")
        r = int(input("Choose your one\nEnter the row: "))
        c = int(input("Enter the column: "))
        if (r, c) in possible_seats and SEATS[r][c] != 0:
            print("Thanks!")
            SEATS[r][c] = 0
        elif (r, c) not in possible_seats:
            r_c_error()
        elif SEATS[r][c] == 0:
            error_taken()
    else:
        print(f"The price is not correct\n the possible prices are {PRICES}")


def main():
    flag = True
    while flag:
        menu = int(input("\nHow do you want to choose your seat?\nFor position [1]\nFor price [2]\nExit [3]\n\t-> "))
        if menu == 1:
            position(SEATS)
        elif menu == 2:
            price(SEATS, PRICES)
        elif menu == 3:
            flag = False
    for i in range(9):
        print(SEATS[i])


def error_taken():
    print("Sorry, the seat is already taken")


def r_c_error():
    print("Error 404\nSeat not found!\nRows are from 0 to 8 | Columns are from 0 to 9")


if __name__ == '__main__':
    main()
