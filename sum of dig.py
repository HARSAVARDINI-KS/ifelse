sum = 0
n = int(input("Enter number:"))
while n > 0:
      digit = n % 10
      n = n//10
      sum = sum + digit
print("The sum of digits of the number is",sum)
