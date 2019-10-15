def count_eights(num_list):
    return num_list.count(8)


def adj(num_list):
    for i, num in enumerate(num_list):
        if(num == 8 and i != len(num_list)-1):
            if(num_list[i+1] == 8):
                return True
    return False




def list_num(list_str):
    num_list = []
    try:
        for element in list_str:
            num_list.append(int(element))
        return num_list
    except:
        print("Error - please enter only integers.")
        return []



def main():
    list_str = input("Enter elements of list separated by commas: ").split(",")

    num_list = list_num(list_str)
    if(num_list != []):
        if(count_eights(num_list) > 1):
            if(adj(num_list)):
                print("True")
            else:
                print("False")
            
        else:
            print("False")

main()