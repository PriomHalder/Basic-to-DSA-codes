def factorial(n:int):
    if n<0:
        return "Error"
    else:
        if n==0:
            return 1
        else:
            return n*factorial(n-1)
