import string

def clean(word):
    word = word.strip()
    word = word.strip(string.punctuation)
    return word



def get_word_list(fstream):
    word_list = []
    for line in fstream:
        temp = line.strip().split()
        for word in temp:
            word = clean(word).lower()
            word_list.append(word)

    return word_list



def word_list_to_counts(word_list):
    word_dict = dict()
    for word in word_list:
        if word in word_dict:
            word_dict[word] += 1
        else:
            word_dict[word] = 1

    return word_dict



def dict_to_tuple(word_count_dict):
    word_count_list = []
    for key, val in word_count_dict.items():
        word_count_list.append((key, val))
    return word_count_list

def main():
    filename = input("Name of file: ")
    # Get a file stream
    fstream = open(filename)
    # Get a list of words from the stream
    word_list = get_word_list(fstream) 
    fstream.close()
    # Transform the list to a dictionary of word-count pairs
    word_count_dict = word_list_to_counts(word_list) 
    # Finally, makes a list of tuples from the dictionary
    word_count_tuples = dict_to_tuple(word_count_dict)
    print(sorted(word_count_tuples))
    
main()