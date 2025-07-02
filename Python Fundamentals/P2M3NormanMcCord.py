# [] test string: `Little fly, Thy summer’s play My thoughtless hand Has brushed away. Am not I A fly like thee? Or art not thou A man like me?`  

def word_mixer(word_list):
    word_list.sort()
    # print(word_list)
    mixed_list = []

    while len(word_list) > 5:
        mixed_list.append(word_list.pop())
        mixed_list.append(word_list.pop(-5))
        mixed_list.append(word_list.pop(0))
        mixed_list.append(word_list.pop())
        
    return mixed_list

poem = input("Welcome Norman McCord enter a saying or poem: ")
poem = poem.split()
poem_len = len(poem)

for i in range(poem_len):
    if len(poem[i]) <= 3:
        poem[i] = poem[i].lower()
    elif len(poem[i]) >= 7:
        poem[i] = poem[i].upper()
    else:
        pass



mixed = word_mixer(poem)
print(" ".join(mixed))

