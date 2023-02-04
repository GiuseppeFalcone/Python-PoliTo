def main():
    SIZE = 3
    player_1 = 0
    player_2 = 'X'

    grid = list()
    for i in range(3):
        t = list()
        for j in range(3):
            t.append(None)
        grid.append(t)

    for x in range(SIZE*SIZE):
        if x % 2 != 0:
            print("00 PLAYER 1 00")
            i = int(input("Insert the coordinates\nRow: "))
            j = int(input("Column"))
            grid[i][j] = 0
            print_grid(grid, SIZE)
            check_winner(grid)
        elif x % 2 == 0:
            print("XX PLAYER 2 XX")
            i = int(input("Insert the coordinates\nRow: "))
            j = int(input("Column"))
            grid[i][j] = 'X'
            print_grid(grid, SIZE)
            check_winner(grid)

def check_winner(grid):
    win = False
    while not win:
        a = b = c = None
        for i in range(3):
            for j in range(3):
                c = grid[i][j]
            if i == 0:
                a = c
            elif i == 1:
                b = c
            if (a == b == c) != None:
                win = True
                if a == 0:
                    print("There is a winner and it is Player 1 !!!!!!!")
                elif a == 'X':
                    print("There is a winner ant it is Player 2 !!!!!!!")



def print_grid(t, SIZE):
    for i in range(SIZE):
        for j in range(SIZE):
            print("| ", end="")
            print(t[i][j], end=" | ")
        print("")


if __name__ == '__main__':
    main()