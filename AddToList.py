
def main():
    user_input = input("Enter value to be added to list: ")
    values = []

    while(user_input != "exit"):
        values.append(user_input)
        user_input = input("Enter value to be added to list: ")
    else:
        values = values*3
        for element in values:
            print(element)        

main()