n=int(input("enter the digit"))
n1 = int(input("Enter First number :"))
n2 = int(input("Enter Second number :"))
x = n1
y = n2
while(n2!=0):
    t = n2
    n1=t
    n2 = n1 % n2
gcd = n1
print(gcd)
lcm = (x*y)/gcd
print(lcm)
