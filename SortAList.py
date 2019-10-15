# sort_list() function goes here
def sort_list(a_list):
    a_list.sort()
    return a_list.sort()
# get_list() function goes here
def get_list():
    a_list = []
    while True:
        try:
            a_int = int(input())
            a_list.append(a_int)
        except ValueError:
            return a_list
# Do not modify this part
def main():
    a_list = get_list()
    print(a_list)
    print(sort_list(a_list))
    print(a_list)
    
main()