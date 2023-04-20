input_string = input("Enter the string: ")
nth_letter = input("Entere the letter: ")
nth_letter_place = input_string.find(nth_letter)
first_string = input_string[:nth_letter_place]
second_string = input_string[nth_letter_place:]
print(first_string[0:]+second_string[1:])
