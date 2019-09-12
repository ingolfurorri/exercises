d = int(input("Type in the exercise you want to run: "))

if(d == 1):
    # find_min function definition goes here
    def find_min(num1, num2):
        if(num1 > num2):
            return num2
        else:
            return num1

    first = int(input("Enter first number: "))
    second = int(input("Enter second number: "))
    
    # Call the function here
    minimum = find_min(first, second)
    print("Minimum: ", minimum)

elif(d == 2):
    # Your function definition goes here

    def upper_fun(user_input):
        upper_count = 0
        for i in user_input:
            if i.isupper():
                upper_count += 1
        return upper_count

    def lower_fun(user_input):
        lower_count = 0
        for i in user_input:
            if i.islower():
                lower_count += 1
        return lower_count

    user_input = input("Enter a string: ")

    # Call the function here

    upper = upper_fun(user_input)
    lower  = lower_fun(user_input)

    print("Upper case count: ", upper)
    print("Lower case count: ", lower)

elif(d == 3):
    e = 2

elif(d == 4):
    e = 2

elif(d == 5):
    e = 2

elif(d == 6):
    e = 2