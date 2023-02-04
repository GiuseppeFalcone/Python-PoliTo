def main():
    n = int(input("Enter an integer value: "))
    raw_numbers = list()
    for i in range(1, n+1):
        raw_numbers.append(i)

    mul_2 = 4
    mul_3 = 6
    while mul_2 in raw_numbers:
        raw_numbers.remove(mul_2)
        mul_2 += 2

    while mul_3 in raw_numbers:
        raw_numbers.remove(mul_3)
        mul_3 += 3

    print(raw_numbers)



if __name__ == '__main__':
    main()
