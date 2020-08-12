def fibonacci (n):
    if n<=1:
        return n
    else:
        return (fibonacci(n-1) + fibonacci(n-2))


if __name__ == "__main__" :
    n= int(input("Enter the number you want to output the fibonacci sequence of: "))
    for n in range (0,n):
        print (fibonacci(n))


