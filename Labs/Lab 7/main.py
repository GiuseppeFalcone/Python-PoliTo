from random import randint
from random import uniform
# # Ex 1
def main():
    nums = []
    for i in range(11):
        nums.append(randint(1, 20))
    print(nums)
    print(f"Even indexes vulues: {even_ind(nums)}\nEqual numbers: {equal_val(nums)}")
    print(f"Reverse order: {reverse(nums)}\nFirst {nums[0]} | Last: {nums[len(nums)-1]}")

def even_ind(nums):
    even_ = []
    for i, e in enumerate(nums):
        if i % 2 == 0 and i > 0:
            even_.append(e)
    return even_

def equal_val(nums):
    equal_ = []
    temp_nums = list(nums)

    for i, e in enumerate(nums):
        for x in range(0, len(temp_nums)-1):
            if e == temp_nums[x]:
                # if e not in equal_:
                equal_.append(e)

    return equal_

def reverse(nums):
    rev_ = []
    for i in range(-1, -(len(nums)-1), -1):
        rev_.append(nums[i])
    return rev_



#######################################################################################
# # Ex 2
# def main():
#     nums = []
#     n = None
#     while n is None or n != -42:
#         n = int(input("To stop the loop enter -42\nEnter a number: "))
#         if n != -42:
#             nums.append(n)
#     print(nums)
#     print(f"The list is: {nums}")
#     alternatingSum(nums)
#
# def alternatingSum(elements):
#     altsum = 0
#     print("The alternating sum: ", end='')
#     for i, val in enumerate(elements):
#         if i % 2 == 0:
#             altsum+=val
#             if (i+1) != len(elements):
#                 print(val, end='-')
#             else:
#                 print(val, end='')
#         elif i % 2 == 1:
#             altsum -= val
#             if (i+1) != len(elements):
#                 print(val, end='+')
#             else:
#                 print(val, end='')
#     print(f"= {altsum}")
##########################################
# # Ex 3
# def main():
#     n = None
#     l_1 = []
#     l_2 = []
#     while n is None or n != -42:
#         print("First List\nTo exit enter -42")
#         n = int(input("Enter a value: "))
#         if n != -42:
#             l_1.append(n)
#     n = None
#     while n is None or n != -42:
#         print("\nSecond List\nTo exit enter -42")
#         n = int(input("Enter a value; "))
#         if n != -42:
#             l_2.append(n)
#
#     value = equal(l_1, l_2)
#     if value:
#         print(f"The two list contain the same elements in the same order ")
#     else:
#         print(f"They don't contain the same elements in the same order")
#
# def equal(a, b):
#     if a == b:
#         return True
#     else:
#         return False
#########################################################################################################
# # Ex 4
# def main():
#     l_1 = []
#     l_2 = []
#     n = None
#     print("\nFirst List\nTo exit enter -42")
#     while n is None or n != -42:
#         n = int(input("Enter a value: "))
#         if n != -42:
#             l_1.append(n)
#
#     n = None
#     print("\nSecond List\nTo exit enter -42")
#     while n is None or n != -42:
#         n = int(input("Enter a value; "))
#         if n != -42:
#             l_2.append(n)
#     same_set(l_1, l_2)
# def same_set(l_1, l_2):
#     temp_1 = []
#     temp_2 = []
#     for i, e in enumerate(l_1):
#         if e not in temp_1:
#             temp_1.append(e)
#     for i, e in enumerate(l_2):
#         if e not in temp_2:
#             temp_2.append(e)
#     temp_1.sort()
#     temp_2.sort()
#     if temp_1 == temp_2:
#         print(f"The two lists have the same values! {temp_1} = {temp_2}")
#     else:
#         print(f"The values {temp_1} abd {temp_2} are not equal")
##########################################################################################
# # Ex 5 & 6
# def main():
#     nums = []
#     for i in range(20):
#         nums.append(randint(0, 99))
#     print(f"The Original list: {nums}")
#     print(f"The List now sorted: {sorted(nums)}")
#     # Ex 6
#     print(f"The list reversed: {nums[::-1]}")
############################################################################################
# # Ex 7
# def main():
#     nums = []
#     for i in range(10):
#         nums.append(randint(0, 50))
#     print("The Original list is", nums)
#     sum_without_smallest(nums)
# def sum_without_smallest(nums):
#     sum_ = 0
#     nums.pop(nums.index(min(nums)))
#     min_ = nums[0]
#     for i, e in enumerate(nums):
#         sum_ += e
#         if min_ > e:
#             min_ = e
#     dif = sum_ - min_
#     print(f"The difference between the sum: {sum_} and the minimum value: {min_} is: {dif}")
#####################################################################################################
# def main():
#     nums = []
#     for i in range(10):
#         nums.append(uniform(0, 100))
#     print("The Original list is", nums)
#     print(f"The values adjusted are:{adjust_vals(nums)}")
#
# def adjust_vals(nums):
#     for i in range(len(nums)):
#         if i == 0:
#             nums[i] = (nums[i]+nums[i+1]) / 2
#         elif i == len(nums) - 1:
#             nums[i] = (nums[i]+nums[i-1]) / 2
#         elif i > 0 or i < len(nums)-2:
#             nums[i] = (nums[i]+nums[i-1]+nums[i+1]) / 3
#     return nums
if __name__ == '__main__':
    main()