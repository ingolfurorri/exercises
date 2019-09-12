def clean(in_str):
    in_str = in_str.lower()
    clean_str = ""

    for i in in_str:
        if (i.isalpha()):
            clean_str += i
    print(clean_str)        
    return clean_str

def is_palindrome(in_str):
    in_str = clean(in_str)

    str_back = in_str[::-1]

    if(in_str == str_back):
        return True
    else:
        return False

in_str = input("Enter a string: ")

str_bool = is_palindrome(in_str)
if(str_bool):
    print(""""{}" is a palindrome.""".format(in_str))

else:
    print(""""{}" is not a palindrome.""".format(in_str))
