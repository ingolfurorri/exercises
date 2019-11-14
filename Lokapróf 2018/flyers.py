def open_file():
    try:
        file_str = 'flights.txt'
        #file_str = input("Enter filename: ")
        input_file = open(file_str, 'r')
        return input_file

    except FileNotFoundError:
        print("File {} not found!").format(file_str)
        return None



def close_file(input_file):
    input_file.close()



def get_sublist(word_list, temp):

    for index, sub_list in enumerate(word_list):
            if temp[0] in sub_list:
                if temp[1] not in sub_list:
                    word_list[index].append(temp[1])
                break

    else:
        word_list.append(temp)




def get_word_list(input_file):
    word_list = []
    for line in input_file:
        line = line.strip()
        temp = line.split()
        get_sublist(word_list, temp)

    return word_list



def get_most_countries(word_list):
    max_length = 0
    max_name = ''
    for sublist in word_list:
        if len(sublist) - 1 > max_length:
            max_length = len(sublist) - 1  
            max_name = sublist[0]

    return [max_name, max_length]


def pretty_print(word_list):
    print_string = ''
    most_countries = get_most_countries(word_list)
    word_list.sort()
    for sublist in word_list:
        print_string += sublist.pop(0) + ': \n'
        sublist.sort()
        for element in sublist:
            print_string += '\t' + element + '\n'
        

    print(print_string)

    print("{} has been to {} countries".format(most_countries[0], most_countries[1]))



def main():
    input_file = open_file()
    if(input_file != None):
        word_list = get_word_list(input_file)
        close_file(input_file)
        pretty_print(word_list)



main()