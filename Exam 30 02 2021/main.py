import sys
IN_FILE = 'strawberry.txt'


def checking_triplets(all_words):
    triplets = list()
    for i in range(len(all_words)-1):
        if len(all_words[i]) == len(all_words[i+1]) == len(all_words[i+2]):
            temp = [all_words[i], all_words[i+1], all_words[i+2]]
            triplets.append(temp)
            print(temp)

def main():
    all_words = list()
    try:
        with open(IN_FILE) as input_file:
            for line in input_file:
                for word in line.rstrip(',.\n\"').split():
                    all_words.append(word.upper())
    except OSError as error:
        print(f"Something went wrong with: {IN_FILE} | {error}")
        sys.exit(10)

    checking_triplets(all_words)


if __name__ == '__main__':
    main()
