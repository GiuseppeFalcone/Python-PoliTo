from string import ascii_uppercase


def cook(a):
    b = list()
    for i in a:
        if i != ' ':
            b.append(i.upper())
    return b


def fun(a, b, other):
    both = list()
    once = list()
    for i in a:
        if i in b:
            both.append(i)
            if i in other:
                other.remove(i)
        elif i not in b:
            once.append(i)
            if i in other:
                other.remove(i)
    return both, once, other


def main():
    phrase_1 = str(input("Enter the first string: "))
    phrase_2 = str(input("Enter the second string: "))
    first = cook(phrase_1)
    second = cook(phrase_2)

    other = list(ascii_uppercase)

    both, once, other = fun(first, second, other)

    print(f"The characters in both strings are: {both}\nThe characters in only one of them are: {once}\nThe characters not in one or another are: {other}")


if __name__ == '__main__':
    main()
