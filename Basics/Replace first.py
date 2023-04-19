first_string = input("Enter the first string: ")
second_string = input("Enter the second string: ")
a = first_string[:2] + second_string[2:]
b = second_string[:2]  + first_string[2:]
print(a+" "+b)
