number=int(input("Enter your number:"))
limit=int(input("Enter your limit:"))

for i in range(1,limit+1):
    print(f"{number}x{i}={number*i}")