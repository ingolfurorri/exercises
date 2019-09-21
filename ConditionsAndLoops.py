example = int(input("Enter the example you want to run: "))

if(example == 3):
    n  = int(input("Enter the number of throws: "))
    m = int(input("Enter the sum: "))
    
    minimum = n
    maximum = n*6

    if(minimum <= m <= maximum):
        print("Yes")
    else:
        print("No")

if example == 6:
    n = int(input("Enter a number: "))

    for i in range(2, n, 2):
        print(i)

if example == 7:
    n = int(input("Enter a number: "))

    for i in range(1, 11):
        for j in range(1, n+1):
            print(j*i, end = '  ')
        print()

if example == 8:
    n = int(input("Input number of lines: "))
    a = int(input("Input a (Fizz): "))
    b = int(input("Input a (Buzz): "))

    for i in range(1, n):
        if(i % a == 0 or i % b == 0):
            if(i % a == 0 and i % b == 0):
                print("FizzBuzz")
                continue
            elif(i % a == 0):
                print("Fizz")
            else:
                print("Buzz")
        else:
            print(i)

if example == 9:

    n = int(input("Enter the iterations: "))
    pi = 0

    for i in range(n+1):
        formerki = (-1)**i
        pi += formerki * (1/(2*i+1))

    print(4*pi)
