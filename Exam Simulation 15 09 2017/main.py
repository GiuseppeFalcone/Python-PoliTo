import sys
INPUT_FILE = 'numbers.txt'


def opening():
    numbers = list()
    try:
        with open(INPUT_FILE, 'r') as file:
            numbers = file.readline().rstrip().split()
    except OSError as error:
        print(f"Error with {INPUT_FILE} | {error}")
        sys.exit(1)
    return numbers


def right_trunck():
    numbers = opening()
    low_limit, high_limit = input("Enter the low limit"), input("Enter the high limit")
    counter = 0
    right_nums = list()
    for i in numbers:
        if low_limit<= int(i) >= high_limit:
            new_num = int(i.replace(i[-1], ''))
            new_num2 = int(new_num.replace(new_num[-1], ''))
            if check_prime(new_num) and check_prime(new_num2):
                counter += 1
                right_nums.append(i)
    print(f"The file contains {counter} right-truncatable prime numbers ")

def check_prime(num):
    temp = True
    for i in range(2, num, 1):
        if num % i == 0:
            temp = False
    return temp


def main():



if __name__ == '__main__':
    main()
