def adding_report(report):
    total = 0
    items = ""
    print('Input an integer to add to the total or "Q" to quit')
    
    while True:
        user_input = input('Enter an integer or "Q": ')
        
        if user_input.isdigit():
            total += int(user_input)
            if report == "A":
                items += user_input + "\n"
        
        elif user_input.upper().startswith("Q"):
            if report == "A":
                print("\nItems")
                print(items)
            print("Total")
            print(" ", total)
            print(" Calculated by: Norman McCord")
            break
        
        else:
            print(user_input, "is invalid input")
    
adding_report("A")
adding_report("T")