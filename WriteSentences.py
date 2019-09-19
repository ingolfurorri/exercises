import string

def clean(word):
    return word.strip()

file_str = input()
file_input = open(file_str, "r")
file_output = open("sentences.txt", "w")

iteration = 0

for word in file_input:
    iteration += 1
    word = clean(word)
    if(iteration == 1):
        print(word, end = '')
        print(word, file=file_output)
    else:
        if(word in string.punctuation):
            if word == '.':
                print(word)
                iteration = 0
                continue
            else:
                print(word, end = ' ')
        else:
            print(' ' + word, end = '')
            print(word, file=file_output)