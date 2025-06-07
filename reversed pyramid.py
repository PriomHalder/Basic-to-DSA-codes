# reversed pyramid 
n=5
i=0
while(i<n):
    j=0
    while (j<=i):
        if j==0:
            pass
        else:
          print(" ",end="")
        j=j+1
    k=0
    while (k<=n-1-i):
        print("* ",end="")
        k=k+1
    print("")
    i=i+1
