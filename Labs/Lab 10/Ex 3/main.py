def main():
    file_names = list()
    file_names = file_naming()
    word_to_search = input("Enter the word to search in the files: ")
    searching(file_names, word_to_search)


def file_naming():
    raw_names = input("Enter all the file names, specifying the file type")
    l = raw_names.split(', ')
    return l


def searching(file_names, word_to_search):
    for file in file_names:
        try:
            with open(file, 'r') as f:
                for line in f:
                    line.rstrip()
                    if word_to_search.lower() in line.lower():
                        print(f"{file}: {line}")
        except OSError as error:
            print(f"Something went wrong with {file}: Error: {error}")


if __name__ == '__main__':
    main()
