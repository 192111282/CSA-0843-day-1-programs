num =int(input("enter the number"))
factorial=1
if num < 0:
   print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
   print("The factorial of 0 is 1")
else:
   for i in range(1,num + 1):
     factorial = factorial*i
try:
    num = int(input())
    print("\nFactors of " +str(num)+ " are: ", end="")
    for i in range(1, num+1):
        if num % i == 0:
            print(i, end=" ")
    print()
except ValueError:
    print("\nInvalid Input!")
