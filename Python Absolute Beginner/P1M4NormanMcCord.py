def str_analysis(user_input):
    if user_input.isdigit():
        number = int(user_input)
        if number > 99:
            print(f"{number} is a big number.")
        else:
            print(f"{number} is a small number.")
    elif user_input.isalpha():
        print(f"{user_input} is all alphabetical characters.")
    else:
        print(f"{user_input} is neither all letters nor all digits.")

# Test the function
user_input = input("Norman McCord, enter a word or integer: ")

while user_input == "":
    user_input = input("Norman McCord, enter a word or integer: ")
    
str_analysis(user_input)

