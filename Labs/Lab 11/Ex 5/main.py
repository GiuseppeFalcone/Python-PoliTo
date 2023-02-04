import sys
IN_FILE_NAME = 'song.txt'
OUT_FILE_NAME = 'corrected_song.txt'
BAD_WORDS = ['sex', 'sesso', 'drugs', 'droga', 'cocaine', 'cocaina', 'violence', 'violenza', 'canna', 'joint',
             'gun', 'arma', 'fuck', 'cazzo', 'fuck you', 'vaffanculo', 'shit', 'merda'
             ]


def opening(in_file):
    raw_words = list()
    try:
        with open(in_file, 'r') as file:
            for line in file:
                line_splitted = line.split()
                line_splitted.append('\n')
                for word in line_splitted:
                    raw_words.append(word)
    except OSError as error:
        print(f"Something went wrong with {in_file}: {error}")
        sys.exit(1)
    print(raw_words)
    return raw_words


def cook(raw_words, bad_words):
    corrected_words = list()
    for word in raw_words:
        if word.lower() not in bad_words:
            corrected_words.append(word)
        elif word.lower() in bad_words:
            corrected_words.append('*'*len(word))
    return corrected_words


def printing(corrected_words, out_file):
    try:
        with open(out_file, 'w') as file:
            for word in corrected_words:
                file.write(f"{word} ")
    except OSError as error:
        print(f"Something went wrong with {out_file}: {error}")
        sys.exit(1)
    return file


def main():
    raw_words = opening(IN_FILE_NAME)
    corrected_words = cook(raw_words, BAD_WORDS)
    printing(corrected_words, OUT_FILE_NAME)


if __name__ == '__main__':
    main()
