import string

def clean(word):
    return word.strip()

file_str = input("Enter filename: ")
file_input = open(file_str, "r")
file_output = open("sentences.txt", "w")

iteration = 0

for word in file_input:
    iteration += 1
    word = clean(word)

    if(iteration == 1):
        print(word, end='')
        continue
    
    if(word == ''):
        print()
        iteration = 0
        continue
    elif(word == '.' or word == ','):
        print(word, end = '')
        print(word, file=file_output)
    else:
        print(' ' + word, end = '')
