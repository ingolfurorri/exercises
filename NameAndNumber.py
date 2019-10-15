def get_tuple(data_dict):
    temp_list = []
    for key, val in data_dict.items():
        temp_list.append((key, val))

    return temp_list




def main():
    more_data = 'y'
    data_dict = {}

    while(more_data == 'y'):
        name = input("Name: ")
        number = input("Number: ")

        data_dict[name] = number

        more_data = input("More data (y/n)? ")

    else:
        print_list = get_tuple(data_dict)
        print(sorted(print_list))



main()