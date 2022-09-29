amount=int(input("enter the amount"))
time=int(input("enter the time"))
customer=int(input("enter the option if you are senior citizen press 1,othewise press 2"))
if(customer==1):
    simple_intrest1=(amount*12*time/100)
    print(simple_intrest1)
elif(customer==2):
        simple_intrest2=(amount*10*time/100)
        print(simple_intrest2)
