my_string="MALAYALAM"
my_string=my_string.casefold()
rev_string=reversed(my_string)
if list(my_string)==list(rev_string):
    print("PALINDROME")
else:
    print("NOT A PALINDROME")
