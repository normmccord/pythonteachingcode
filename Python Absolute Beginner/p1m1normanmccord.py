# Create name check code

# [ ] get input for input_test variable
input_test = input("Enter names of people you met in the last 24 hours: ").lower()

# [ ] print "True" message if "John" is in the input or False message if not
print("Is John in the list?", "john" in input_test.lower())

# [ ] print True message if your name is in the input or False if not
print("Is Norm in the list?", "norm" in input_test.lower())

# [ ] Challenge: Check if another person's name is in the input - print message
print("Is Mary in the list?", "mary" in input_test.lower())

# [ ] Challenge: Check if a fourth person's name is in the input - print message
print("Is Bob in the list?", "bob" in input_test.lower())