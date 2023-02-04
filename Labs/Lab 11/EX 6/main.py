FILE_NAME = 'rawdata_2004.txt'


def main():
    """Entry point"""
    countries = dict()
    try:
        with open(FILE_NAME, 'r') as file_in:
            for raw_line in file_in:
                line = raw_line.rstrip()
                first_block, income = line.rsplit(maxsplit=1)
                line_number, country = first_block.split(maxsplit=1)
                value = int(income[1:].replace(',', ''))
                countries[country] = value
    except OSError as exception:
        print(f"There's an error: [{exception}]")

    # Sorted by Key
    for i in sorted(countries):
        print(f"{i} -> {countries[i]}")

    print()

    # Sorted by Item
    for i in sorted(countries, key=lambda i: countries[i], reverse=True):
        print(f"{i} -> {countries[i]}")


if __name__ == '__main__':
    main()
