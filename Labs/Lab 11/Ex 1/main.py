FILE_NAME = 'song.txt'


def main():
    words = dict()
    try:
        with open(FILE_NAME, 'r') as file:
            for line in file:
                line.strip('\'\"(),.?!')
                a = line.split()
                for i in a:
                    if i not in words:
                        words[i] = 0
                        words[i] += 1
                    elif i in words:
                        words[i] += 1
    except OSError as error:
        print(f"Something went wrong {error}")

    sort_words = sorted(words.items(), key=lambda x: x[1], reverse=True)
    for i in range(100):
        for x in sort_words:
            print(x[0], x[1])


if __name__ == '__main__':
    main()
