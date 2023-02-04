import sys
from string import ascii_lowercase
FILENAME = 'song.txt'
OUTPUTFILE = 'dictionary.txt'


def main():
    """Main Entry Point"""
    words = list()
    try:
        with open(FILENAME) as input_file:
            for line in input_file:
                for raw_words in line.split():
                    words.append(cook(raw_words))
    except OSError as exception:
        print(f"Something went wrong {FILENAME}: {exception}")
        sys.exit(10)

    words_dict = dict()
    for letter in ascii_lowercase:
        words_dict[letter] = set()

    for word in words:
        for letter in word:
            words_dict[letter].add(word)

    try:
        with open(OUTPUTFILE, 'w') as output_file:
            for letter in ascii_lowercase:
                if words_dict[letter]:
                    output_file.write(f"Words containing '{letter}':\n")
                    for word in sorted(words_dict[letter]):
                        output_file.write(f"\t{word}\n")
                    output_file.write("\n")
    except OSError as error:
        print(f"Something went wrong woth {OUTPUTFILE} : {error}")
        sys.exit(10)


def cook(raw):
    cooked = raw.lower()
    cooked = cooked.strip(' \n"\'+-,.?!')
    return cooked


if __name__ == '__main__':
    main()
