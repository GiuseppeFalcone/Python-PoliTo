name = input("Enter a string")

print(name[0]+ name[1] + name[2], end='')
print("...", end='')
length = len(name)
print(name[length-3], end='')
print(name[length-2], end='')
print(name[length-1], end='')
