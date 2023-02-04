from sys import exit
CLASSES = 'classes.txt'


def open_each_file(class_code, id_num):
    try:
        with open(f'/mnt/HDD Linux/Dropbox (Politecnico Di Torino Studenti)/Computer Science Programs/Labs/Lab 10/Ex 7/classes/{class_code}', 'r') as file:
            for line in file:
                temp = line.rstrip().split(' ')
                if id_num == temp[0]:
                    print(f"{class_code.replace('.txt', '')} {temp[1]}")
    except OSError as error:
        print(f"There was an error with the file: {class_code} | {error} ")
        exit(1)


def open_classes(id_num):
    try:
        with open(CLASSES, 'r') as file:
            for line in file:
                class_code = line.rstrip() + '.txt'
                open_each_file(class_code, id_num)
    except OSError as error:
        print(f"There was an error with the file: {CLASSES} | {error} ")
        exit(1)


def main():
    finish_flag = True
    print("Enter the ID number that you want to check\nTo exit enter 00")
    while finish_flag:
        id_num = input("Enter the ID number: ")
        if id_num != '00':
            open_classes(id_num)
        else:
            finish_flag = False


if __name__ == '__main__':
    main()
