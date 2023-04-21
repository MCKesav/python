input_string = input("Enter the string: ")
nth_number = int(input("Entere the nth number: "))
first_string = input_string[:nth_number]
second_string = input_string[nth_number:]
print(first_string[0:]+second_string[1:])
