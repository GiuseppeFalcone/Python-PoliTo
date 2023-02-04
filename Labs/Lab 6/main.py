def main():
    name = input("Enter a string")
    # Ex 1
    print(f"In this string there are {count_vowels(name)} vowels")
    # Ex 2
    print(f"In this string there are {count_words(name)} words")
    # Ex 3
    find(name)
    # Ex 4
    sentinel = input("Do you want to start the calculus of financial aid? [y/n] -> ")
    while sentinel != -1:
        children_aid()
        sentinel = input("To exit the program enter -1")

# Ex 1
def count_vowels(name):
    counter = 0
    vowels = 'aeiouAEIOU'
    for i, e in enumerate(name):
        if e in vowels:
            counter += 1
    return counter

# Ex 2
def count_words(name):
    counter = 0
    for i, e in enumerate(name):
        if e == ' ':
            if i < len(name) - 2 and name[i+1] != ' ':
                counter += 1
        if i == len(name) - 1:
            counter += 1
    return counter

# Ex 3
def find(name):
    match = input("Enter a string")
    if match in name:
        print("The string is contained in the previous one")
    else:
        print("The string is not contained in the previous one")

# Ex 4
def children_aid():
    benefit = 0
    income = float(input("Enter the annual income: "))
    children = int(input("Enter the number of children: "))
    if income >= 30000 and income <= 40000 and children >= 3:
        benefit = 1000 * children
    elif income >= 20000 and income <= 30000 and children >= 2:
        benefit = 1500 * children
    elif income < 20000 and children > 0:
        benefit = 2000 * children
    print(f"The financial aid is {benefit}$")




if __name__ == '__main__':
    main()
