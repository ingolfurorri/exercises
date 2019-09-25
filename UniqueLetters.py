import string

def remove_pun(sentence):
    clean = []
    for char in sentence:
        if char not in string.punctuation:
            clean.append(char)

    return clean

# Implement a function here
def create_list(sentence):
    sentence_list = list(sentence)
    if ' ' in sentence_list:
        for i in range(sentence_list.count(' ')):
            sentence_list.remove(' ')
    return sentence_list

def unique_letters(sentence):
    '''Returns a list with unique letters'''
    unique = []
    for char in sentence:
        if char not in unique:
            unique.append(char)

    return unique


# Main starts here
sentence = input("Input a sentence: ")

sentence = create_list(sentence)

clean_list = remove_pun(sentence)

unique = unique_letters(clean_list)

print("Unique letters:", unique)
