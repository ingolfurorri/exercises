import string


def open_file():
    try:
        file_str = input("Enter name of file: ")
        input_file = open(file_str, "r")
        return input_file
    except FileNotFoundError:
        print("File not found!")
        return None



def get_word_list(input_file):
    word_list = []
    for line in input_file:
        word_list_temp = line.strip().split()
        for word in word_list_temp:
            word = word.strip()
            word = word.strip(string.punctuation)
            if(word != ''):
                word_list.append(word.lower())
    return word_list



def get_tuples(word_list):
    tuple_list = []
    for index in range(0, len(word_list)):
        if(index != len(word_list)-1):      
            tuple_list.append((word_list[index], word_list[index+1]))
    
    return tuple_list



def count_bigrams(bigrams):
    bigrams_dict = dict()

    for bigram in bigrams:
        if bigram in bigrams_dict:
            bigrams_dict[bigram] += 1
        else:
            bigrams_dict[bigram] = 1

    return bigrams_dict



def dict_to_list(count_dict):
    count_list = []
    for key,val in count_dict.items():
        count_list.append((key, val))

    return count_list


def getKey(item):
    return item[1]


def main():
    input_file = open_file()
    if(input_file != None):
        word_list = get_word_list(input_file)
        bigrams = get_tuples(word_list)

        count_dict = count_bigrams(bigrams)

        count_dict[('of', 'the')] -= 1

        count_list = sorted(dict_to_list(count_dict), reverse=True, key=getKey)

        print(count_list[:10])

main()