def clean(word):
    return word.strip()

def word_length(word):
    return len(word)


#Main program

file_str = input("Enter filename: ")
input_file = open(file_str, "r")
word_win = ''
word_length_max = 0

for word in input_file:
    word = clean(word)
    word_len = word_length(word)

    if(word_len > word_length_max):
        word_length_max = word_len
        word_win = word

print("Longest word is '{}' of length {}".format(word_win, word_length_max))
