def main():
    """Main Entry Point"""
    # print("Point A")
    # point_a()
    # print("\nPoint B")
    # point_b()
    # print("\nPoint C")
    # point_c()
    # print("\nPoint D")
    # point_d()
    # print("\nPoint E")
    # point_e()
    # print("\nPoint F")
    # point_f()
    # print("\nPoint G")
    # point_g()
    # print("\nPoint I")
    # point_i()
    print("\nPoint J")
    point_j()

# def point_a():
#     a = list()
#     flag = False
#     print("Enter the values\nTo stop entering values insert -9")
#     while not flag:
#         n = int(input("Enter a value: "))
#         if n != -9:
#             a.append(n)
#         else:
#             flag = True
#     print(f"Original list: {a}\nSwapped list: {swap(a)}")
#
#
# def swap(a):
#     """Point a function Swapping"""
#     x = a[0]
#     y = a[-1]
#     a[0] = y
#     a[-1] = x
#     b = list()
#     b = a
#     return a


# def point_b():
#     a = list()
#     flag = False
#     print("Enter the values\nTo stop entering values insert -9")
#     while not flag:
#         n = int(input("Enter a value: "))
#         if n != -9:
#             a.append(n)
#         else:
#             flag = True
#     print(f"Original list: {a}\nShifted list: {shift(a)}")
#
#
# def shift(a):
#     x = a.pop()
#     a.insert(0, x)
#     b = a
#     return b


# def point_c():
#     a = list()
#     flag = False
#     print("Enter the values\nTo stop entering values insert -9")
#     while not flag:
#         n = int(input("Enter a value: "))
#         if n != -9:
#             a.append(n)
#         else:
#             flag = True
#     print(f"Original list: {a}\nList with even numbers replaced by 0: {repl_even(a)}")
#
#
# def repl_even(a):
#     for i in range(len(a)-1):
#         if a[i] % 2 == 0:
#             a[i] = 0
#     b = a
#     return b


# def point_d():
#     a = list()
#     flag = False
#     print("Enter the values\nTo stop entering values insert -9")
#     while not flag:
#         n = int(input("Enter a value: "))
#         if n != -9:
#             a.append(n)
#         else:
#             flag = True
#     print(f"Original list: {a}\nList with numbers replaced with largest neighbourhood: {repl_neighbourhood(a)}")
#
#
# def repl_neighbourhood(a):
#     b = a
#     for i in range(1, len(a)-1, 1):
#         if a[i-1] > a[i+1]:
#             b[i] = a[i-1]
#         elif a[i+1] > a[i-1]:
#             b[i] = a[i+1]
#     return b


# def point_e():
#     a = list()
#     flag = False
#     print("Enter the values\nTo stop entering values insert -9")
#     while not flag:
#         n = int(input("Enter a value: "))
#         if n != -9:
#             a.append(n)
#         else:
#             flag = True
#     print(f"Original list: {a}\nList with numbers in the middle removed: {rmv_middle(a)}")
#
#
# def rmv_middle(a):
#     if len(a) % 2 != 0:
#         a.pop(len(a)//2)
#     elif len(a) % 2 == 0:
#         x = a[len(a)//2]
#         y = a[(len(a)//2)-1]
#         a.remove(x)
#         a.remove(y)
#     return a


# def point_f():
#     a = list()
#     flag = False
#     print("Enter the values\nTo stop entering values insert -9")
#     while not flag:
#         n = int(input("Enter a value: "))
#         if n != -9:
#             a.append(n)
#         else:
#             flag = True
#     print(f"Original list: {a}\nList with even numbers in front: {move_even(a)}")
#
#
# def move_even(a):
#     for i in range(0, len(a), 1):
#         if a[i] % 2 == 0:
#             x = a[i]
#             a.pop(a.index(x))
#             a.insert(0, x)
#     return a


# def point_g():
#     a = list()
#     flag = False
#     print("Enter the values\nTo stop entering values insert -9")
#     while not flag:
#         n = int(input("Enter a value: "))
#         if n != -9:
#             a.append(n)
#         else:
#             flag = True
#     print(f"Original list: {a}\nSecond Largest Number: {second_largest(a)}")
#
#
# def second_largest(a):
#     a.remove(max(a))
#     return max(a)


# def point_h():
#     a = list()
#     flag = False
#     print("Enter the values\nTo stop entering values insert -9")
#     while not flag:
#         n = int(input("Enter a value: "))
#         if n != -9:
#             a.append(n)
#         else:
#             flag = True
#
#
# def check_sort(a):
#     for i in range(1, len(a)):
#         if a[i-1] > a[i]:
#             flag = True
#         else:
#             flag = False
#     if flag:
#         print("The list is not sorted")
#     else:
#         print("The list is sorted")


# def point_i():
#     a = list()
#     flag = False
#     print("Enter the values\nTo stop entering values insert -9")
#     while not flag:
#         n = int(input("Enter a value: "))
#         if n != -9:
#             a.append(n)
#         else:
#             flag = True
#     check_adjacent(a)
#
#
# def check_adjacent(a):
#     flag_dup = False
#     i = 1
#     while i < len(a):
#         if a[i-1] == a[i]:
#             print(f"There are 2 adjacent duplicate: {a[i-1]} and {a[i]}")
#             flag_dup = True
#         i += 1
#     if not flag_dup:
#         print("The list does not contain any adjacent duplicate")


def point_j():
    a = list()
    flag = False
    print("Enter the values\nTo stop entering values insert -9")
    while not flag:
        n = int(input("Enter a value: "))
        if n != -9:
            a.append(n)
        else:
            flag = True
    check_duplicate(a)


def check_duplicate(a):
    duplicate = list()
    flag = None
    i = 0
    while i < len(a):
        for num in a:
            b = a
            b.remove(num)
            for x in range(len(b)):
                if b[x] == num:
                    flag = True
                    duplicate.append(b[x])
    if flag:
        print(f"The duplicates are: {duplicate}")
    else:
        print("There are no duplicate")

if __name__ == '__main__':
    main()
