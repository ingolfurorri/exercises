import string



def clean(word):
    word.strip()
    if word[-1] in string.punctuation:
        if word[-1] and word[-2] in string.punctuation:
            return word[:-2]

        if word[0] in string.punctuation:
            return word[1:-1]

        return word[:-1]

    if word[0] in string.punctuation:
        return word[1:]

    else:
        return word
    
    

def unique_words(words_list):
    words_list_unique = []
    for word in words_list:
        if word not in words_list_unique:
            words_list_unique.append(word)
    return words_list_unique



def get_words(input_file):
    words_list = []
    for line in input_file:
        temp = line.split()
        for word in temp:
            word = clean(word)
            words_list.append(word)

    return words_list



def word_list(input_file):
    words_list = get_words(input_file)
    words_list_unique = unique_words(words_list)
    print(sorted(words_list_unique))

    input_file.close()



def main():
    try:
        input_file_str = input("Enter filename: ")
        input_file = open(input_file_str, "r")
        word_list(input_file)

    except FileNotFoundError:
        print("File not found!")



main()