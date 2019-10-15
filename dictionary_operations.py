def menu_selection():
    print("Menu: ")
    choice = input("add(a), remove(r), find(f): ")
    return choice



def add_to_dict(a_dict):
    key = input("Key: ")
    val = input("Value: ")

    if key not in a_dict:
        a_dict[key] = val
    else:
        print("Error. Key already exists.")



def remove_from_dict(a_dict):
    key = input("key to remove: ")

    if key not in a_dict:
        print("Key not found.")
    
    else:
        a_dict.pop(key)



def find_key(a_dict):
    key = input("Key to locate: ")

    if key not in a_dict:
        print("Key not found.")
    else:
        print("Value:", a_dict[key])



def execute_selection(choice, a_dict):
    if(choice == 'a'):
        add_to_dict(a_dict)

    elif(choice == 'r'):
        remove_from_dict(a_dict)

    elif(choice == 'f'):
        find_key(a_dict)



def dict_to_tuples(a_dict):
    dict_list = []
    for key, val in a_dict.items():
        dict_list.append((key, val))
    
    return dict_list

# Do not change this main function
def main():
    more = True
    a_dict = {}
    
    while more:      
        choice = menu_selection()
        execute_selection(choice, a_dict)
        again = input("More (y/n)? ")
        print(a_dict)
        more = again.lower() == 'y'
    
    dictlist = dict_to_tuples(a_dict)
    print(sorted(dictlist))

main()