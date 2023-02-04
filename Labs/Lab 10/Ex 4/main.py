FILE_NAME = 'input.txt'


def main():
    sales = dict()
    all_correct = False
    try:
        with open(FILE_NAME, 'r') as file:
            for line in file:
                a = line.split(';')
                a.pop(-1)
                name, service, amount = a
                name = name.strip()
                service = service.strip()
                amount = float(amount)
                print(f"[{name}] [{service}] [{amount}]")

                if not name or not service or type(amount) != float:
                    raise ValueError("Can't split line")

                if service not in sales:
                    sales[service] = 0.0
                    sales[service] += amount
        all_correct = True
    except OSError as error:
        print(f"There was an error with {FILE_NAME}: {error}")
    except ValueError as error:
        print(f"Wrong format! {error}")

    if all_correct:
        for i in sorted(sales):
            print(f"{i:20}: {sales[i]:10}")
    else:
        print("There was a problem")

if __name__ == '__main__':
    main()
