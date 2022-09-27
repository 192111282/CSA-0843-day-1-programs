x=int(input("enter the first number"))
n=int(input("enter the second number"))
option=int(input("enter the option"))
if(option==1):
    a=x+n
    print("the addition of x and n is",a)
elif(option==2):
    s=x-n
    print("the subtraction of x and n is",s)
elif(option==3):
    m=x*n
    print("the multiplication of x and n is",m)
elif(option==4):
     d=x/n
     print("the division of x and n is",d)
elif(option==5):
     p=pow(x,n)
     print("the power of x and n is",p)
else:
      print(failed)
