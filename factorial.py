n=int(input("ENTER A NUMBER:"))
fact=1
if n<0:
    print("INVALID NUMBER")
elif n==0:
    print("THE FACTORIAL IS 1")
else:
    for i in range(1,n+1):
        fact=fact*i
    print("THE FACTORIAL IS :",fact)
