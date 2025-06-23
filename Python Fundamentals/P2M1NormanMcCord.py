# Norman McCord
# P2M1 required code

fam_quote = input("enter a 1 sentence quote, non-alpha separate words: ")
word = ""

for i in fam_quote:
    if i.isalpha():
        word += i
    else:
        if word != "" and word[0].lower() > "g":
            print(word.upper())
        word = ""

if word != "" and word[0].lower() > "g":
    print(word.upper())
