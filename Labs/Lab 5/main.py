def main():
    ## Ex 1
    # names = []
    # name = input("Enter a name")
    # while name != "":
    #     names.append(name)
    #     name = input("Enter a name")
    #
    # # names_sorted = sorted(names, reverse=True) # sort the objects of an array, from numbers to strings
    # #                                       # Reverse is False, if then made True it will sort the objects in reverse mode, from 10 to 1 fro example
    # # for n in names_sorted:
    # #     print(n)
    #
    # # Another way
    # len_names_array = len(names)
    # for i in range(len_names_array - 1):
    #     j = i + 1
    #     while j <= len_names_array - 1:
    #         if names[i] > names[j]:
    #             p = names[i]
    #             names[i] = names[j]
    #             names[j] = p
    #         j += 1
    #
    # for n in names:
    #     print(n)
##########################################################################################
    # # EX 2
    # CORRECT_PIN = "1234"
    # number_of_tries = 0
    # the_end = False
    #
    # pin = input("Enter the pin: ")
    #
    # while not the_end and number_of_tries < 3:
    #     if pin == CORRECT_PIN:
    #         print("The pin is correct")
    #         the_end = True
    #     else:
    #         print("The pin is incorrect")
    #         number_of_tries += 1
    #         if number_of_tries == 3:
    #             print("Your bank ard is blocked")
    #         else:
    #             pin = input("Enter the pin")
#############################################################################
    # # EX 3
    # number = int(input("Enter a number: "))
    # factor = 2
    #
    # while number > 1:
    #     if number % factor == 0:
    #         print(factor)
    #         number /= factor
    #     else:
    #         factor += 1
##################################################################################
    # # EX 4
    # a = 32310901
    # b = 1729
    # m = 2 ** 24
    #
    # r_old = int(input("Insert initial value: "))
    #
    # for i in range(100):
    #     r_new = (a * r_old + b) % m
    #     print(r_new)
    #     r_old = r_new
########################################################################################
    # # EX 5
    # prey_old = int(input("Initial size of the prey population: "))
    # pred_old = int(input("Initial size of the predator population: "))
    # a = float(input("A: Rate: The prey birth exceeds natural death: "))
    # b = float(input("B: Rate: predation: "))
    # c = float(input("C: Rate: predator death exceed births without food: "))
    # d = float(input("D: Rate: predator increase in the presence of food: "))
    #
    # periods = int(input("Please specify the number of periods: "))
    #
    # for i in range(periods):
    #     prey_new = prey_old * (1 + a - b * pred_old)
    #     pred_new = pred_old * (1 - c + d * prey_old)
    #     print("-------period %d--------" %(i+1))
    #     print(f"Prey population size: {int(prey_new)}")
    #     print(f"Predators population size: {int(pred_new)}")
    #     prey_old = prey_new
    #     pred_old = pred_new
###########################################################################################
    # # # EX 6
    # name = input("Enter a country name, but in french: ")
    # name = name.capitalize()    # It capitalizes the name in order to make life easier
    # name_lenght = len(name)     # Gets the lenght of the name
    #
    # # The exceptions, even thou they are feminine words, we put le
    # exceptions = ["Belize", "Cambodge", "Mexique", "Mozambique", "Zaire", "Zimbabwe"]
    # # Vocals in order to check the first character
    # vocals = "aeiouAEIOU"
    #
    # # Check if it's a plural country name
    # y = False
    # for i in range(name_lenght):
    #     if name[i] == '-':
    #         y = True
    # if y:
    #     print(f"Les {name}")
    # else:
    #     # for loop in order to check in the exceptions
    #     x = False
    #     for i in range(5):
    #         if name == exceptions[i]:
    #             x = True
    #     if x:
    #         print(f"Le {name} x = True")
    #     else:
    #         if name[0] in vocals:     # Check if first character is a vocal
    #             print(f"L'{name}")
    #         elif name[name_lenght - 1] == 'e':      # Check if it is feminine
    #             print(f"La {name}")
    #         elif name[name_lenght - 1] != 'e':      # Check if it is mascuiline
    #             print(f"Le {name}")
###################################################################################
    # EX 7
    buyers = 0
    remaining_tickets = 100
    max_demand = 4
    while remaining_tickets > 0:
        buyers += 1
        demand = int(input("How many tickets do you want?"))
        while demand > max_demand:
            demand = int(input("\nThe maximum number of tickets per each is 4\nEnter the new number of tickets: "))
        remaining_tickets -= demand
        print(f"The remaining tickets are {remaining_tickets}")
        if remaining_tickets <=3:
            max_demand = remaining_tickets
    print(f"The total number of buyers was {buyers}")

if __name__ == '__main__':
    main()
