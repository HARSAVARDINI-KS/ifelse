list1=[3,5,1,7,9,8,6,2,4,10]
length=len(list1)
flag='True'
for i in range(0,length):
        for j in range (i+1,length):
            if list1[i]+ list1[j]==15:
                print(i,j)
                break
                break
                break
            
