def to_int(a_list):
    int_list = []
    for i in a_list:
        int_list.append(int(i))
    return int_list

def even_list(a_list):
    return [i for i in a_list if not i%2]

def even_sum(a_list):
    a_list = to_int(a_list)
    a_list_even = even_list(a_list)
    return sum(a_list_even)


def get_list():
    a_list = input("Enter elements of list separated by commas: ").strip().split(',')
    return a_list

# Main program starts here - DO NOT change it
a_list = get_list()
print(even_sum(a_list))
