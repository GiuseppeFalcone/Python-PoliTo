import mm


def main():
    maze, possible_path = mm.main()
    for i in range(len(maze)):
        for j in range(len(maze[i])):
            if maze[i][j] == ' ':
                maze[i][j] = '?'
    maze[0][1] = 'N'
    maze[8][-2] = 'S'
    for i in range(len(maze)):
        print(maze[i])

    for i in range(len(maze)):
        for j in range(len(maze[i])):
            if maze[i][j] == '?':
                if (i, j) in possible_path:
                    for x in possible_path[(i, j)]:
                        if x[0] > 0 and x[1] == 1:
                            maze[i][j] = 'N'
                        if x[0] > 0 and 1 < x[1] <


    for i in possible_path:
        print(f"{i} -> {possible_path[i]}")





if __name__ == '__main__':
    main()
