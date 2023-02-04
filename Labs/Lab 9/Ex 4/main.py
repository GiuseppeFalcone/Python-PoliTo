def main():
    numbers = list()
    print("\t\tInseting all the values of the list\nTo exit inert 9999")
    num = int(input("Enter a number: "))
    while num != 9999:
        numbers.append(num)
        num = int(input("Enter a number: "))

    minimum, maximum = remove_min(numbers)
    print(f"Minimum = {minimum}\nMaximum = {maximum}")


def remove_min(numbers):
    minimum = numbers[0]
    maximum = numbers[-1]
    for i in numbers:
        if i < minimum:
            minimum = i
        elif i > maximum:
            maximum = i
    return minimum, maximum


if __name__ == '__main__':
    main()
