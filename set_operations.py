def get_list():
    set1_str = set(input("Input a list of integers separated with a comma: ").split(","))
    set1 = set([int(i) for i in set1_str])
    return set1



def get_intersection(set1, set2):
    set3 = set1 & set2
    print(set3)



def get_union(set1, set2):
    set3 = (set1 | set2)
    print(set3)


def get_difference(set1, set2):
    set3 = (set1.difference(set2))
    print(set3)


def get_user_input(set1, set2):
    print('''1. Intersection
2. Union
3. Difference
4. Quit''')

    user_input = int(input("Set operation: "))

    if user_input == 1:
        get_intersection(set1, set2)
        return True

    elif user_input == 2:
        get_union(set1, set2)
        return True

    elif user_input == 3:
        get_difference(set1, set2)
        return True

    elif user_input == 4:
        return False



def main():
    set1 = get_list()
    set2 = get_list()

    print(set1)
    print(set2)

    while(get_user_input(set1, set2)):
        continue


main()