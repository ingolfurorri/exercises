def bigger_num(num1, num2):
    '''Returns the bigger number'''
    if(num1 > num2):
        return num1
    else:
        return num2

#Main program
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

print("The bigger number of {} and {} is {}".format(num1, num2, bigger_num(num1, num2)))