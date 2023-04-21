input_string = input("Enter the string: ")
first_string = input_string[:2]
middle_string = input_string[2:-2]
second_string = input_string[-2:]
print(second_string+middle_string+first_string)
