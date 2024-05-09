# def add(n1,n2):
#     a=n1+n2
#     print("sum is " ,a)
# add(5,6)

# def div(n1,n2):
#     a=n1/n2

#     print("result is " ,a)
# div(5,6) 

import random
n=int(input('enter limit  '))
character ="abcdeABCDF1234#$@"
password =""
for i in range (1,n+1):
    password+=random.choice(character)
print(password)