# # Ex 1
# # 1. Write programs that read a sequence of integer inputs and print
# # a. The smallest and largest of the inputs.
# # b. The number of even and odd inputs.
# # c. Cumulative totals. For example, if the input is 1 7 2 9, the program should print
# # 1 8 10 19.
# # d. All adjacent duplicates. For example, if the input is 1 3 3 4 5 5 6 6 6 2, the
# # program should print 3 5 6.
#
sequence = input("enter a sequence of integer numbers: ")
# A
print(f"The maximum is {max(sequence)}")
# B
print(f"The minimum is {min(sequence)}")

# C
print()
total = 0
for i in range(len(sequence)):
    total += int(sequence[i])
    print(total, end=' ')
print(f"\nThe cumulative total is {total}")

# D ????


######################################################################################
# # Ex 2
# # 2. Write programs that read a line of input as a string and print
# # a. Only the uppercase letters in the string.
# # b. Every second letter of the string.
# # c. The string, with all vowels replaced by an underscore.
# # d. The number of digits in the string.
# # e. The positions of all vowels in the string.
#
# line = input("Please enter the line: ")
#
# # a
# i = 0
# while i < len(line):
#     # Using the Asci table
#     # hex_value = ord(line[i])
#     # if hex_value >= 0x41 and hex_value <= 0x5A:   # (0x YYYYY) in order to use hexadecimal
#     # Using .isupper
#     if line[i].isupper():
#         print(line[i], end='_')
#     i += 1
#
# # b
# print()
# for i in range(0, len(line), 1):
#     if i % 2 == 1 and line[i-1].isalpha():
#         print(f"The {i + 1} letter is {line[i]}")
#
# # c
# print()
# vowels = "aeiouAEIOU"
# for i in range(0, len(line), 1):
#     if line[i] in vowels and line[i].isalpha():
#         print('_', end='')
#     elif line[i].isalpha():
#         print(line[i], end='')
#
# # D
# print()
# for i in range (0, len(line), 1):
#     if line[i].isnumeric():
#         n += 1
# print(f"The number of digits is {n}")
#
# # E
# print()
# for i in range (0, len(line), 1):
#     if line[i] in vowels and line[i].isalpha():
#         print(f"The vowel is in position {i+1}")

################################################################################################################
# # 3. Write a program that reads an integer and displays, using asterisks, a square and a filled diamond
# # of the given side length. For example, if the side length is 4, the program should display:
# # ****
# # ****
# # ****
# # ****
# #  *
# #  ***
# # *****
# # *******
# # *****
# #  ***
# #  *
#
# side = int(input("Enter the side value: "))
#
# # Square
# for i in range(side):
#     print()
#     for x in range(side):
#         print("*", end='')
#
# # Diamond
# if userInput > 0:              # Prevents the computation of negative numbers
#     for i in range(userInput):
#         for s in range (userInput - i) :    # s is equivalent to to spaces
#             print(" ", end="")
#         for j in range((i * 2) - 1):
#             print("*", end="")
#         print()
#     for i in range(userInput, 0, -1):
#         for s in range (userInput - i) :
#             print(" ", end="")
#         for j in range((i * 2) - 1):
#             print("*", end="")
#         print()
#######################################################################################################################
# # 4. Write a program that reads a word and prints the word in reverse. For example, if the
# # user provides the input "Harry", the program prints:
# # yrraH
#
# word = input('Enter a word: ')
#
# for i in range(len(word), 0, -1):
#     print(word[i-1], end='')
#################################################################################################################
# # 5. Prime numbers. Write a program that prompts the user for an integer and then prints
# # out all prime numbers up to that integer. For example, when the user enters 20, the
# # program should print
# # 2357
# # 11
# # 13
# # 17
# # 19
# # Recall that a number is a prime number if it is not divisible by any number except 1 and itself
#
# num = int(input("Enter a number: "))
# for i in range(2, num+1, 1):
#     if i == 2 or i == 3:
#         print(i)
#     elif i % 2 != 0 and i % 3 != 0:
#         print(i)
#############################################################
# 6. Write a program that reads a word and prints all substrings, sorted by length. For example, if the
# user provides the input "rum", the program prints:
# r
# u
# m
# ru
# um
# rum

# word = input('Enter a word: ')
# statement = False
#
# for i in range(len(word)):
#     print(word[i])
# for x in range(len(word)):
#     print(word[i], word[i+1])
##########################################################################################