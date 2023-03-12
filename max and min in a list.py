list1=[]
n=int(input("enter the number of numbers"))
for i in range (n):
    num=int(input("enter the number"))
    list1.append(num)
print("largest num=" , max(list1))
print("smallest num=" , min(list1))
