ALPHABET = ' ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
ROT = 13


def chr2num(c):
    return ALPHABET.index(c)


def num2chr(c):
    return ALPHABET[(len(ALPHABET) + c) % len(ALPHABET)]


def encrypt(string):
    encrypted = ""
    for c in string:
        encrypted += num2chr(chr2num(c) + ROT)
    return encrypted


def decrypt(string):
    plain = ""
    for c in string:
        plain += num2chr(chr2num(c) - ROT)
    return plain


def main():
    string = input()
    enc = encrypt(string)
    dec = decrypt(enc)
    print(f"'{string}' -> '{enc}' -> '{dec}'")


if __name__ == '__main__':
    main()
