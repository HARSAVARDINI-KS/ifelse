list1=[]
list2=[]
sum=0
n=int(input("enter the number of numbers"))
for i in range (n):
    num=int(input("enter the number"))
    list1.append(num)
for j in list1:
    if j%2 == 0:
        sum=sum+j
        #list2.append(j)
print("sum of even digits:" , sum)
