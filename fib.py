num=int(input("Enter number of fib series"))
a=0
b=1
c=1
if num==1:
    print(a)
elif num==2:
    print(a,b)
elif num>2:
    print(a,b,end=" ")
    for i in range(num-2):
            print(c,end=" ")
            a=b
            b=c
            c=a+b
    


