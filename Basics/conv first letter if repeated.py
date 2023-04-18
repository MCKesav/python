input_string = input ("Enter the word: ")
first_string = input_string[0]
second_string = input_string[1:]
print(first_string + second_string.replace(first_string,"$"))
