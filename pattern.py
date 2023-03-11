num = int(input("enter the number:"))
for i in range(num):
    for j in range(0,i+1):
        print("*",end="")
    print()
num1 = int(input("enter the number:"))
for i in range(num):
    for j in range(0,i+1):
        print(chr(65+j),end="")
    print()
