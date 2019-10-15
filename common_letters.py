def get_common_list(name):
    common_list = []
    first = name[0].lower()
    last = name[1].lower()
    if name[0] > name[1]:
        for ch in first:
            if ch in first and ch in last and ch not in common_list:
                common_list.append(ch)
    
    else:
        for ch in last:
            if ch in first and ch in last and ch not in common_list:
                common_list.append(ch)

    return common_list

def get_common_set(name):
    first_set = set(name[0].lower())
    last_set = set(name[1].lower())
    
    return first_set & last_set

def main():
    name = input("Enter name: ").strip().split()

    common_list = get_common_list(name)

    common_set = get_common_set(name)

    print(sorted(common_list))

    print(sorted(common_set))


main()