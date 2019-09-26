#list_to_tuple function goes here
def to_int(element):
    try:
        element = int(element)
        return element
    except ValueError:
        return None

def list_to_tuple(a_list):
    tuple_list = []
    for element in a_list:
        if(to_int(element) == None):
            empty_tuple = ()
            print("Error. Please enter only integers.")
            return empty_tuple
        else:
            tuple_list.append(to_int(element))
    return tuple(tuple_list)


# Main program starts here - DO NOT change it
a_list = input("Enter elements of list separated by commas: ").strip().split(',')
a_tuple = list_to_tuple(a_list)
print(a_tuple)