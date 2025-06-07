import math

n= int(input("Enter your number:"))

if n<1:
    print("Error: Please enter a positive integer")
else:
    if n == 1:
        print(f"{n} is not a prime number")
    elif n == 2:
        print(f"{n} is a prime number")

    else:
        for i in range(2,n):
            if (n%i)==0:
                print(f"{n} is not a prime number")
                break
        else:
            print(f"{n} is a prime number")
