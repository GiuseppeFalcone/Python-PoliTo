INPUT_FILE_NAME = 'input.txt'
OUTPUT_FILE_NAME = 'output.txt'


def main():
    lines = list()
    try:
        with open(INPUT_FILE_NAME, 'r') as input_file:
            for line in input_file:
                line.rstrip()
                lines.append(f"{line}")
            print(lines)
            # swapping(lines)
    except OSError as error:
        print(f"Something went wrong: {error}")
    try:
        with open(OUTPUT_FILE_NAME, 'w') as output_file:
            for i in range(len(lines)-1, -1, -1):
                output_file.write(lines[i])
    except OSError as error:
        print(f"Something went wrong: {error}")

# def swapping(lines):
#     for i in range(len(lines)):
#         a = lines.pop(i)
#         lines.insert(len(lines), a)
#     return lines
if __name__ == '__main__':
    main()
