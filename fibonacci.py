def fib(n):
    '''We find and return the appropriate fibonacci number'''
    if(n == 1 or n == 2):
        return 1
    else:
        return fib(n-2) + fib(n-1)

#Main program
n = int(input("How many Fibonacci numbers do you want to see? "))

for i in range (1, n+1):
    print(fib(i), end = ' ')
