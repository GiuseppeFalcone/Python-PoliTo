MAZE_NAME = 'maze.dat'


def creating_maze():
    maze = list()
    try:
        with open(MAZE_NAME, 'r') as maze_description:
            for line in maze_description:
                x = line.strip()
                maze.append(list(x))
    except OSError as exception:
        print(f"There's a problem: {exception}")
    return maze


def path(maze):
    maze_dictionary = dict()
    for r in range(len(maze)):
        for c in range(len(maze[r])):
            if maze[r][c] == ' ':
                maze_dictionary[(r, c)] = set()
                if r > 0 and maze[r - 1][c] == ' ':
                    maze_dictionary[(r, c)].add((r - 1, c))
                if r < len(maze) - 1 and maze[r + 1][c] == ' ':
                    maze_dictionary[(r, c)].add((r + 1, c))
                if c > 0 and maze[r][c - 1] == ' ':
                    maze_dictionary[(r, c)].add((r, c - 1))
                if c < len(maze[r]) - 1 and maze[r][c + 1] == ' ':
                    maze_dictionary[(r, c)].add((r, c + 1))
    return maze_dictionary


def main():
    """Entry point"""
    maze = creating_maze()
    possible_path = path(maze)
    return maze, possible_path


if __name__ == '__main__':
    main()
