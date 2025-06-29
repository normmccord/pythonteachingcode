# [x] create list-o-matic as a function and call it
# [x] be sure to include your spelled-out name in the welcome prompt
# [x] you are welcome to use any list you like for list-o-matic, does not have to be animals 
author_name = "Norman McCord"

# [x] if string is in the list it removes the first instance from list
# [x] if string is not in the list the input gets appended to the list
# [x] if the string is empty then the last item is popped from the list
# [x] if the list becomes empty the program ends
# [x] if the user enters "quit" then the program ends

def list_o_matic(movie_input,movie_list):
    if movie_input == "":
        popped = movie_list.pop()
        return f"{popped} popped from the list."
    elif movie_input in movie_list:
        movie_list.remove(movie_input)
        return f"1 instance of {movie_input} removed from the list."
    else:
        movie_list.append(movie_input)
        return f"{movie_input} added to the list."

movie_list = ["Hackers","Inception","Alien"]


while movie_list:
    print(f"Welcome, {author_name}. Look at all the movies:",movie_list)
    movie_input = input("Enter the name of a movie (or quit). Movies are case-sensitive: ")
    if movie_input.lower() == "quit":
        break

    print(list_o_matic(movie_input,movie_list))


print("Goodbye.")