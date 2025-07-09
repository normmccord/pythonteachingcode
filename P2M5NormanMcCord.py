# Norman McCord


import urllib.request

# Download file and read
url = "https://raw.githubusercontent.com/MicrosoftLearning/intropython/master/elements1_20.txt"
filename = "elements1_20.txt"
urllib.request.urlretrieve(url, filename)

# Read file line-by-line
element_list = []
file = open(filename, "r")
line = file.readline()
while line:
    element_list.append(line.strip().lower())
    line = file.readline()
file.close()

# Get 5 unique user inputs
def get_names():
    inputs = []
    print("Welcome Norman McCord, list any 5 of the first 20 elements in the Periodic Table.")
    while len(inputs) < 5:
        entry = input("Enter the name of an element: ").strip().lower()
        if entry == "q":  # the instructions didn't account for the user deciding to just quit, so I put this here. Still grades inputs based on 5 answers. Ex: if you enter 3 right answers and quit, you'll only get 60%.
            break
        elif entry == "":
            continue
        elif entry in inputs:
            print(f"{entry.title()} was already entered")
        else:
            inputs.append(entry)
    return inputs

# Compare user input with element list using range()
def check_answers(user_answers, valid_elements):
    correct = []
    incorrect = []
    for i in range(len(user_answers)):
        answer = user_answers[i]
        if answer in valid_elements:
            correct.append(answer.title())
        else:
            incorrect.append(answer.title())
    return correct, incorrect

# Run quiz
quiz_answers = get_names()
correct_answers, incorrect_answers = check_answers(quiz_answers, element_list)
score = len(correct_answers) * 20

# Print results
print(f"\n{score} % correct")
print("Found:", " ".join(correct_answers))
print("Not Found:", " ".join(incorrect_answers))
