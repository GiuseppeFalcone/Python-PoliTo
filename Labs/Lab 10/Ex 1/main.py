import sys
INPUT_FILE_NAME = 'input.txt'
OUTPUT_FILE_NAME = 'output.txt'


def main():
    try:
        with open(INPUT_FILE_NAME, 'r') as input_file:
            try:
                with open(OUTPUT_FILE_NAME, 'w') as output_file:
                    i = 0
                    for line in input_file:
                        i += 1
                        output_file.write(f"/*{i}*/ {line}")
            except OSError as error:
                print(f"Something went wrong with {OUT_FILE_NAME}: {error}")
                sys.exit(10)
    except OSError as error:
        print(f"Something went wrong with {INPUT_FILE_NAME}: {error}")
        sys.exit(10)


if __name__ == '__main__':
    main()
