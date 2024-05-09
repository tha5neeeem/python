# def myfunctn ():
#     print('hi')
# myfunctn() 
# def myfunctn(num1,num2):
#     print(num1+num2)

# myfunctn(5,10)    

# def nida(num):
#     a=num*num
#     print("sqrt of num=",a)
# nida(5)
 
# def thechu(a,b):
#     for i in range(1,b):
#      c=i*a
#     print(f'{i}*{a}={c}')
# thechu(3,5)    
# def myfunc(a,b,num):
#     print(a)
#     print(b)
#     for i in range(2,num+1):
#      c=a+b
#      a=b
#      b=c
#      print(c)

# heyy(0,1,7)


# number= int(input("enter a number to find its factorial: "))
# factorial=1
# if number<0:
#     print("factorial is not defined for negative numbers")
# elif number==0 or number==1:
#      print("factorial of ",number,"is 1")
# else:
#      for i in range (2,number+1):
#           factorial *=i
#           print("factorial of ",number,"is ",factorial)
          
# def funcn1(num):
#  if  num==0 or num==1:
#   return 1
#  else:
#   return num * funcn1(num-1)
# print(funcn1(5)
def pwr(a,n):
    if n==0:
        return 1
    else:
        return a*pwr(a,n-1)
print(pwr(2,3))    
        



